import streamlit as st
from pdf2image import convert_from_path
import pytesseract
import os
import tempfile

def pdf_to_text(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

st.title('PDF to Text Converter')

uploaded_file = st.file_uploader('Choose a PDF file', type='pdf')

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name
    
    if st.button('Convert PDF to Text'):
        text = pdf_to_text(pdf_path)
        st.text_area('Extracted Text:', text)
        os.unlink(pdf_path) # Delete the temporary file
