import os
import shutil

image_file=["png","jpeg","jpg"]
pdf_files=["pdf","PAdES"]
office_files=["docx","csv","xlsx"]
code_files=["py","cpp","c","js","php"]

files=os.listdir()
if "main.py" in files:    
    files.remove("main.py")
for file in files:
    if(file.split(".")[-1] in image_file):
        if not os.path.exists("images"):
            os.makedirs("images")
        shutil.move(file,"images")
    elif(file.split(".")[-1] in pdf_files):
        if not os.path.exists("PDF Files"):
            os.makedirs("PDF Files")
        shutil.move(file,"PDF Files")
    elif(file.split(".")[-1] in office_files):
        if not os.path.exists("Office Files"):
            os.makedirs("Office Files")
        shutil.move(file,"Office Files")
    elif(file.split(".")[-1] in code_files):
        if not os.path.exists("Coding Files"):
            os.makedirs("Coding Files")
        shutil.move(file,"Coding Files")
    else:
        if not os.path.exists("Others"):
            os.makedirs("Others")
        shutil.move(file,"Others")
    