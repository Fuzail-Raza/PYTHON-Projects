from PyPDF2 import PdfReader,PdfWriter
import os

path=os.listdir("E:\Programms\PYTHON\exercises\pdf_files")

merger = PdfWriter()
for files in path:
    merger.append(f"E:\Programms\PYTHON\exercises\pdf_files\{files}")
merger.write("merged-pdf.pdf")
merger.close()