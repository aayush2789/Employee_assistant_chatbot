from langchain.docstore.document import Document
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def create_vector_store(user_data_str, embeddings, emp_id, base_dir):
    documents = [Document(page_content=user_data_str, metadata={'source': 'session_data'})]
    persistent_dir = os.path.join(base_dir, f"user_{emp_id}")
    db = Chroma.from_documents(documents, embeddings, persist_directory=persistent_dir)
    return persistent_dir

def get_vector_store(persistent_dir, embeddings):
    return Chroma(persist_directory=persistent_dir, embedding_function=embeddings)

def create_vector_store_res(docs, embeddings, emp_id, base_dir):
    persistent_dir=os.path.join(base_dir,f"resume_{emp_id}")
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=100,chunk_overlap=10
    )
    doc_chunks=text_splitter.split_documents(docs)
    db=Chroma.from_documents(doc_chunks,embeddings,persist_directory=persistent_dir)
    return persistent_dir