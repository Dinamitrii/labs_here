import os

import pdfplumber
from docx import Document


pdf = pdfplumber.open(os.path.join(os.path.dirname(__file__), "static/pdf", "lekar.pdf"))
doc = Document()

for page in pdf.pages:
    text = page.extract_text()
    if text:
        doc.add_paragraph(text)

doc.save("static/doc/lekar.docx")
pdf.close()

print(os.listdir(os.path.join(os.path.dirname(__file__), "static")))