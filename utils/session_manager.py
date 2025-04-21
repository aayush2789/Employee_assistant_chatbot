import streamlit as st

def init_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if "user_data" not in st.session_state:
        st.session_state.user_data = {}
    if "show_chat" not in st.session_state:
        st.session_state.show_chat=False
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {
            "Name": "Not Provided",
            "Email": "Not Provided",
            "Phone": "Not Provided",
            "Department": "Not Provided",
            "Employee ID": "Not Provided",
            "Office Location": "Not Provided",
            "Resume Uploaded": False,
            "Resume File Name": None
        }
