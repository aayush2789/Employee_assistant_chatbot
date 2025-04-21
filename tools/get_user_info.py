

import streamlit as st
from utils.vector_store import get_vector_store
from utils.embeddings import get_embeddings

def get_user_info(query: str) -> str:
    
    embeddings=get_embeddings()
    try:
        persistent_dir = st.session_state.get('persistent_dir')
        persistent_res_dir=st.session_state.get('persistent_res_dir') # Replace with actual
        
        db_user = get_vector_store(persistent_dir, embeddings)
        db_res = get_vector_store(persistent_res_dir, embeddings)

        user_retriever = db_user.as_retriever(search_type="similarity", search_kwargs={"k": 1})
        user_info = user_retriever.get_relevant_documents(query)

        res_retriever = db_res.as_retriever(search_type="similarity", search_kwargs={"k": 1})
        res_info = res_retriever.get_relevant_documents(query)

        user_docs_text = "\n\n".join([doc.page_content for doc in user_info])
        res_docs_text = "\n\n".join([doc.page_content for doc in res_info])

        
        
        return user_docs_text,res_docs_text

    except Exception as e:
        return f"Error retrieving info: {str(e)}"

