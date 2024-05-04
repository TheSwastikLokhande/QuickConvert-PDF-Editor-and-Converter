
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_path):
    old_pdf = convert_from_path(pdf_path, poppler_path=r"C:\Users\Swastik\PycharmProjects\pythonProject\Release-24.02.0-0\poppler-24.02.0\Library\\bin")
    for i, page in enumerate(old_pdf):
        page.save(f"{output_path}/new{i}.jpg", "JPEG")

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)

def convert_pdf():
    pdf_path = pdf_entry.get()
    output_path = output_entry.get()
    convert_pdf_to_images(pdf_path, output_path)
    result_label.config(text="Conversion completed successfully!")

# GUI setup
app = tk.Tk()
app.title("PDF to Image Converter")

# Widgets
tk.Label(app, text="Select PDF file:").grid(row=0, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(app, width=40)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Select output folder:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(app, width=40)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(app, text="Convert", command=convert_pdf).grid(row=2, column=0, columnspan=3, pady=20)

result_label = tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Run the GUI
app.mainloop()
