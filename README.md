# Employee Assistant Chatbot

This is an AI-powered chatbot built using **Streamlit**, **LangChain**, and **Groq’s Chat Model**. It assists employees by answering queries, scheduling meetings, and organizing documents in a conversational and user-friendly way.

---

## Features

- Collects employee information via a structured form
- Embeds and stores user data and resumes using a vector database
- Responds to queries using RAG (Retrieval-Augmented Generation)
- Organizes documents into categories using a file classification tool
- Schedules meetings using JSON-based availability data

---

## Project Structure

-temp_resumes/ All resumes uploaded by users via the form are stored here.

-sample_docs/ This folder contains files the user wants to organize. The chatbot classifies and organizes these documents into appropriate subfolders.

-components/ Contains UI components such as the form and chat interface

-tools/ Includes tools for file classification, user info retrieval, and meeting scheduling

-db/ contains user info and resume info in form of embeddings(vector store/database)

-prompts/ prompt template for the chatbot

-utils/ Contains utility functions for vector DB management, embedding, and validation

-app.py Main logic for the chatbot interface and interaction

-config.py Api Keys required 



## Notes

- Resumes are uploaded and saved to the `temp_resumes/` folder.
- Documents to be organized should be placed in the `sample_docs/` folder.
- Organized files are palced in sample_docs/organized_files/{desired category}
- User information is stored locally for now; future updates may include database integration.
