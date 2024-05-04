import os
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFPageNumberApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PDF Page Number Adder")
        self.geometry("400x300")
        self.minsize(400,300)
        self.maxsize(400,300)

        self.input_file_path = ""
        self.output_file_path = ""
        self.start_page_number = 1

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select PDF file to add page numbers:").pack(pady=10)

        tk.Button(self, text="Browse", command=self.browse_file).pack()

        tk.Label(self, text="Start page number:").pack(pady=10)
        self.page_number_entry = tk.Entry(self)
        self.page_number_entry.pack()

        tk.Button(self, text="Add Page Numbers", command=self.add_page_numbers).pack(pady=20)

    def browse_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.input_file_path:
            tk.Label(self, text=f"Selected file: {os.path.basename(self.input_file_path)}").pack()

    def add_page_numbers(self):
        if not self.input_file_path:
            messagebox.showerror("Error", "Please select a PDF file.")
            return

        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not self.output_file_path:
            return

        try:
            self.start_page_number = int(self.page_number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid start page number.")
            return

        try:
            self.add_numbers_to_pdf(self.input_file_path, self.output_file_path, self.start_page_number)
            messagebox.showinfo("Success", f"Page numbers added successfully. Saved as: {self.output_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def add_numbers_to_pdf(self, input_file_path, output_file_path, start_page_number):
        with open(input_file_path, "rb") as ifile, open(output_file_path, "wb") as ofile:
            reader = PdfReader(ifile)
            writer = PdfWriter()

            c = canvas.Canvas("temp.pdf", pagesize=letter)

            for i in range(len(reader.pages)):
                page = reader.pages[i]
                c.drawString(10, 10, f"Page {i + start_page_number}")
                c.showPage()

            c.save()

            watermark = PdfReader("temp.pdf")

            for i in range(len(reader.pages)):
                page = reader.pages[i]
                page.merge_page(watermark.pages[i])

            writer.append_pages_from_reader(reader)
            writer.write(ofile)

            os.remove("temp.pdf")

if __name__ == "__main__":
    app = PDFPageNumberApp()
    app.mainloop()
