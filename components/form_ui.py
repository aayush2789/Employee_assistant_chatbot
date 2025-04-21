import streamlit as st
import os
from utils.validators import validate_email, validate_phone,is_duplicate_employee_id
from utils.vector_store import create_vector_store,create_vector_store_res
from utils.embeddings import get_embeddings
from config import BASE_DB_DIR
from langchain_community.document_loaders import PyMuPDFLoader

def user_form():
    embeddings=get_embeddings()

    with st.form("user_form"):
        name = st.text_input("👤 Name")
        email = st.text_input("📧 Email")
        phone = st.text_input("📱 Phone Number")
        department = st.text_input("🏢 Department")
        emp_id = st.text_input("🆔 Employee ID")
        location = st.text_input("📍 Office Location")
        resume = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])

        submit = st.form_submit_button("Submit")

        if submit:
            

            st.session_state.submitted = True
            st.session_state.user_data["Name"] = name if name.lower()!="" else "Not Provided"
            st.session_state.user_data["Email"] = email if email.lower()!="" and validate_email(email) else "Not Provided"
            st.session_state.user_data["Phone"] = phone if phone.lower()!="" and validate_phone(phone) else "Not Provided"
            st.session_state.user_data["Department"] = department if department.lower()!="" else "Not Provided"
            st.session_state.user_data["Employee ID"] = emp_id if emp_id.lower()!="" else "Not Provided"
            
            st.session_state.user_data["Office Location"] = location if location.lower()!="" else "Not Provided"
            user_data = st.session_state.user_data
            emp_id = user_data["Employee ID"]
            
            if is_duplicate_employee_id(emp_id):
                st.warning(f"Employee ID '{emp_id}' already exists. Please use a unique ID.")
                return

            if resume:
                st.session_state.user_data["Resume Uploaded"] = True
                st.session_state.user_data["Resume File Name"] = resume.name
                
                save_path = f"temp_resumes/{resume.name}"
                os.makedirs("temp_resumes", exist_ok=True)

                with open(save_path, "wb") as f:
                    f.write(resume.getbuffer())
                
                loader=PyMuPDFLoader(save_path)
                docs=loader.load()
                persistent_res_dir=create_vector_store_res(docs,embeddings,emp_id,BASE_DB_DIR)
                st.session_state.persistent_res_dir=persistent_res_dir

            
            
            user_data_str = "\n".join([f"{k}: {v}" for k, v in user_data.items()])
            persistent_dir = create_vector_store(user_data_str,embeddings,emp_id,BASE_DB_DIR)
            
            st.session_state.persistent_dir = persistent_dir
            
            st.rerun()
    