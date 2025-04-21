import streamlit as st
from components.form_ui import user_form
from components.chat_ui import chat_box
from utils.session_manager import init_session_state

init_session_state()
if not st.session_state.submitted:
    with st.chat_message("AI"):
        st.markdown("👋 Hi! Before we start, could you please fill out this quick form so I can assist you better?")

    st.title("Employee Information Form")
    user_form()
elif not st.session_state.show_chat:
    
    user_name=st.session_state.user_data.get('Name','there')
    st.success(f'Hi {user_name}!Your details were submitted successfully.')
    with st.chat_message("AI"):
        st.markdown('Click the button to start chatting!')
    if st.button('Continue to Chatbot'):
        st.session_state.show_chat=True
        st.rerun()

else:
    st.title("Employee Assistance Chatbot")
    
    with st.chat_message("AI"):
        user_name = st.session_state.user_data.get("Name", "there")
        st.markdown(f"Hi {user_name}! 👋 How can I help you today?")

    chat_box()
