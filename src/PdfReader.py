
from PyPDF2 import PdfReader
import sys
import os



def OrderExtractor():
    folder_path = os.path.join(os.path.dirname(__file__), '..', 'temp')  # Correct folder path
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    if pdf_files:
        pdf_file_path = os.path.join(folder_path, pdf_files[0])  # Use the first PDF file in the folder
        reader = PdfReader(pdf_file_path)
    else:
        print("No PDF files found in the folder.")
        return ""

    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text = text.replace("FNF CUT-LIST", "")
    
    print(f"Extracted text from {pdf_file_path}")
    return text

