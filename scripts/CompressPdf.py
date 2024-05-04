import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog

def compress_pdf(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }

    gs = get_ghostscript_path()
    initial_size = os.path.getsize(input_file_path)
    subprocess.call([
        gs,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS={}".format(quality[power]),
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-sOutputFile={}".format(output_file_path),
        input_file_path,
    ])
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    return ratio, final_size

def get_ghostscript_path():
    gs_names = ["gs", "gswin32", "gswin64"]
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(
        f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
    )

class PDFCompressorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PDF Compressor")
        self.geometry("400x300")
        self.minsize(400,300)
        self.maxsize(400,300)

        self.input_file_path = ""
        self.output_file_path = ""
        self.compression_level = tk.IntVar(value=2)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Select PDF file to compress:").pack(pady=10)

        tk.Button(self, text="Browse", command=self.browse_file).pack()

        tk.Label(self, text="Compression Level:").pack(pady=10)

        for level, label_text in enumerate(["Default", "Prepress", "Printer", "Ebook", "Screen"]):
            tk.Radiobutton(self, text=label_text, variable=self.compression_level, value=level).pack(anchor="w", padx=20)

        tk.Button(self, text="Compress PDF", command=self.compress_pdf).pack(pady=20)

    def browse_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.input_file_path:
            tk.Label(self, text=f"Selected file: {os.path.basename(self.input_file_path)}").pack()

    def compress_pdf(self):
        if not self.input_file_path:
            tk.messagebox.showerror("Error", "Please select a PDF file to compress.")
            return

        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not self.output_file_path:
            return

        try:
            ratio, final_size = compress_pdf(self.input_file_path, self.output_file_path, self.compression_level.get())
            tk.messagebox.showinfo("Success", f"Compression complete.\nCompression ratio: {ratio:.0%}\nFinal file size: {final_size / 1000000:.5f} MB")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = PDFCompressorApp()
    app.mainloop()
