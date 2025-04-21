import pandas as pd
import streamlit as st

WORK_HOURS = list(range(9, 18))
LUNCH_BREAK = set(range(13, 15))

def parse_time_slots(slot_str):
    if pd.isna(slot_str):
        return []
    blocked = []
    for ts in slot_str.split(", "):
        try:
            h = int(ts.split(":")[0])
            blocked.append((h, h + 1))
        except:
            continue
    return blocked

def get_available_slots(blocked):
    blocked_hours = set()
    for start, end in blocked:
        blocked_hours.update(range(start, end))
    return [(h, h + 1) for h in WORK_HOURS if h not in blocked_hours and h not in LUNCH_BREAK]



def get_meeting_slot(csv_path="employee_schedules.csv"):
    df = pd.read_csv(csv_path)
    df.set_index(df.columns[0], inplace=True)

    schedule = {}

    for emp in df.index:
        schedule[emp] = {}
        for date in df.columns:
            blocked = parse_time_slots(df.loc[emp, date])
            available = get_available_slots(blocked)
            schedule[emp][date] = available

    return schedule
