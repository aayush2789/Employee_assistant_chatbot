from utils.model import llm
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os
import shutil



def classify_files(file_names):
    prompt = PromptTemplate.from_template("""
        You are an intelligent file classifier. Classify these filenames into clear categories like 'Finance', 'HR', 'Marketing' and 'Tech'.

        Filenames:
        {file_list}

        Return a JSON object where the key is the category and the value is a list of files.
        Return ONLY valid JSON like this:
        {{
        "Finance": ["file1.pdf", "file2.xlsx"],
        "HR": ["file3.docx"]
        }}""")

    chain = prompt | llm | StrOutputParser()
    joined_names = "\n".join(file_names)
    response = chain.invoke({'file_list':joined_names})
    return response

def organize_files(classification_dict, base_folder="sample_docs"):
    for category, files in classification_dict.items():
        category_folder = os.path.join(base_folder, 'organized_files' , category)
        os.makedirs(category_folder, exist_ok=True)
        for file in files:
            src = os.path.join(base_folder, file)
            dst = os.path.join(category_folder, file)
            if os.path.exists(src):
                shutil.move(src, dst)