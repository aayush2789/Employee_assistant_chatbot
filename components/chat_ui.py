import streamlit as st
import json
import os
import re
from prompts.template import user_prompt
from utils.model import llm
from langchain.schema.output_parser import StrOutputParser
from tools.get_user_info import get_user_info
from tools.get_slot import get_meeting_slot
from utils.streaming import StreamlitCallbackHandler
from tools.file_classifier import classify_files,organize_files

def chat_box():
    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

    user_query = st.chat_input("Your message")
    if user_query:
        
        st.session_state.chat_history.append(("Human", user_query))
        with st.chat_message("Human"):
            st.markdown(user_query)

        if "organize documents" in user_query.lower():
            file_list = os.listdir("sample_docs")  
            llm_response = classify_files(file_list)
            
            cleaned = re.sub(r"```json|```", "", llm_response).strip()
            classified_dict=json.loads(cleaned)
            st.write(classified_dict)
            organize_files(classification_dict=classified_dict)
            
            response = "📁 Documents have been organized into their respective folders."
            with st.chat_message("AI"):
                st.markdown(response)
            st.session_state.chat_history.append(("AI", response))
            return
        

        user_docs_text,res_docs_text=get_user_info(user_query)
        schedule=get_meeting_slot()
        schedule_json=json.dumps(schedule)
        with st.chat_message("AI"):
            stream_container=st.empty()
            callback=StreamlitCallbackHandler(stream_container)
        
        try:
            streaming_llm=llm
            chain=user_prompt | streaming_llm | StrOutputParser()
            response = chain.invoke({"user_query":user_query,"user_info":user_docs_text,"resume_info":res_docs_text,'input_json':schedule_json}
                                    ,config={"callbacks":[callback]})
            stream_container.markdown(response)
            st.session_state.chat_history.append(("AI", response))
            
        except Exception as e:
            st.error(f"❌ Error: {e}")

        

        
