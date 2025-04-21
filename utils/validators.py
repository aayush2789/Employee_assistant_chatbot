import re
import os
from config import BASE_DB_DIR
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone)

def is_duplicate_employee_id(emp_id: str) -> bool:
    
    emp_dir = os.path.join(BASE_DB_DIR, "user_"+emp_id)
    return os.path.exists(emp_dir)