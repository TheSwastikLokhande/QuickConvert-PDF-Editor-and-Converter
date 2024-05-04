import subprocess
from tkinter import *
from PIL import Image, ImageTk
# Initialize the main window
window = Tk()
window.geometry("800x600")
window.minsize(800, 600)
window.maxsize(800, 600)


def open_Slipt_Pdf():
    subprocess.Popen(['python', 'splitPdf.py'])


def open_Merge_Pdf():
    subprocess.Popen(['python', 'pdfMerge.py'])


def open_Compress_Pdf():
    subprocess.Popen(['python', 'CompressPdf.py'])


def open_Protect_Pdf():
    subprocess.Popen(['python', 'protectpdf.py'])

def open_Word_To_Pdf():
    subprocess.Popen(['python', 'word_to_pdf_converter.py'])

def open_img_To_Pdf():
    subprocess.Popen(['python', 'imageToPdf.py'])

def open_pdf_To_img():
    subprocess.Popen(['python', 'pdftoimg.py'])
def open_addPageNumber():
    subprocess.Popen(['python', 'addPageNumbersToPdf.py'])

def open_ppt_to_pdf():
    subprocess.Popen(['python', 'ppttopdf.py'])

def open_imageConverter():
    subprocess.Popen(['python', 'imageConverter.py'])

lable_space = Label(window,
                    text="                                                                                        ")
lable_space.grid(row=0, column=0)
# Title
title = Label(window, text="Quick Convert, Edit", font=("Times New Roman", 20, "bold"), fg="blue")
title.grid(row=0, column=1, pady=50)

# Merge Pdf

Merge_pdf_button = Button(window, text="Merge Pdf", font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                          relief="groove", bd=5, command=open_Merge_Pdf)
Merge_pdf_button.grid(row=1, column=0)
# split pdf button

split_pdf = Button(window, text="Split Pdf", font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                   relief="groove", bd=5, command=open_Slipt_Pdf)
split_pdf.grid(row=1, column=1)

# Compress pdf
Compress_pdf_button = Button(window, text="Compress Pdf", font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                             relief="groove", bd=5, command=open_Compress_Pdf)
Compress_pdf_button.grid(row=1, column=2)

# lable_spac1 = Label(window,
#                     text="                                                                                        ")
lable_space.grid(row=2, column=0)

# Protect Pdf
Protect_pdf_button = Button(window, text="Protect pdf", font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                            relief="groove", bd=5, command=open_Protect_Pdf)
Protect_pdf_button.grid(row=3, column=0)

# Word to pdf
wordToPdf_button=Button(window,text="Word To Pdf", font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                            relief="groove", bd=5, command=open_Word_To_Pdf)
wordToPdf_button.grid(row=3,column=1)

# Image To Pdf
img_to_pdf_button=Button(window,text="img to pdf",font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                            relief="groove", bd=5, command=open_img_To_Pdf)
img_to_pdf_button.grid(row=3,column=2)

lable_space1=Label(window,text="   ")
lable_space1.grid(row=4,column=0)

# Pdf To Image
pdf_to_image_button=Button(window,text="pdf to image",font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                            relief="groove", bd=5, command=open_pdf_To_img)
pdf_to_image_button.grid(row=5,column=0)


# add page numbers
addPageNumbersToPdf_button=Button(window,text="Add page number to pdf",font=("Century Schoolbook", 14, "bold"), width=15, height=2,
                            relief="groove", bd=5, command=open_addPageNumber,wraplength=200)
addPageNumbersToPdf_button.grid(row=5,column=1)

# ppt To pdf
ppt_to_pdf=Button(window,text="PPT To Pdf",font=("Century Schoolbook", 14, "bold"), width=15, height=1,
                            relief="groove", bd=5, command=open_ppt_to_pdf)
ppt_to_pdf.grid(row=5, column=2)

lable_space2=Label(window,text="   ")
lable_space2.grid(row=6,column=0)

# image converter
iamge_Converter= Button(window,text="Image Converter",font=("Century Schoolbook", 14, "bold"),width=15, height=1,
                            relief="groove", bd=5, command=open_imageConverter)
iamge_Converter.grid(row=7,column=1)
window.mainloop()
