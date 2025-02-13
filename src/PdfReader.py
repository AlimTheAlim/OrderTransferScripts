
from PyPDF2 import PdfReader
import os

def OrderExtractor():
    folder_path = "repos/FFAutoOrder/temp/"
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    if pdf_files:
        pdf_file_path = os.path.join(folder_path, pdf_files[0])  # You can modify to pick a specific file if needed
        reader = PdfReader(pdf_file_path)
    else:
        print("No PDF files found in the folder.")
    
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text =""
    for page in reader.pages:
        text+= page.extract_text()
    text = text.replace("FNF CUT-LIST","")
    
    return text

