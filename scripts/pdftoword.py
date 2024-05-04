# from pdf2docx import Converter
#
# old_pdf="E:\My p doc\Diploma Lc.pdf"
# new_doc = "lc.docx"
#
# obj = Converter(old_pdf)
# obj.convert(new_doc)
# obj.close()
#

import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    obj = Converter(pdf_path)
    obj.convert(docx_path)
    obj.close()

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

def browse_output_folder():
    folder_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    docx_entry.delete(0, tk.END)
    docx_entry.insert(0, folder_path)

def convert_pdf():
    pdf_path = pdf_entry.get()
    docx_path = docx_entry.get()

    if pdf_path and docx_path:
        convert_pdf_to_docx(pdf_path, docx_path)
        result_label.config(text="Conversion completed successfully!")
    else:
        result_label.config(text="Please select PDF and output DOCX paths.")

# GUI setup
app = tk.Tk()
app.title("PDF to DOCX Converter")

# Widgets
tk.Label(app, text="Select PDF file:").grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(app, width=40)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Select output DOCX file:").grid(row=1, column=0, padx=10, pady=10)
docx_entry = tk.Entry(app, width=40)
docx_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(app, text="Convert", command=convert_pdf).grid(row=2, column=0, columnspan=3, pady=20)

result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Run the GUI
app.mainloop()
