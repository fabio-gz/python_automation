#!/usr/bin/python3
"""
Combining select pages from PDFs
"""
import PyPDF2
import os

pdfFile = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFile.append(filename)

pdfFile.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFile:
    pdfobj = open(filename, 'rb')  # read binary
    pdfreader = PyPDF2.PdfFileReader(pdfobj)
    for pageNum in range(1, pdfreader.numPages):
        pageobj = pdfreader.getPage(pageNum)
        pdfWriter.addPage(pageobj)

pdfoutput = open(filename, 'wb')
pdfWriter.write(pdfoutput)
pdfoutput.close()
