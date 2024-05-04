import tkinter as tk
from tkinter import filedialog, messagebox
import pptxtopdf

# Function to convert PPT or PPTX to PDF
def convert_to_pdf():
    # Ask the user to select a PPT or PPTX file
    ppt_file_path = filedialog.askopenfilename(
        title="Select PowerPoint File",
        filetypes=[("PowerPoint files", "*.ppt;*.pptx")]
    )

    if not ppt_file_path:
        return  # If no file is selected, do nothing

    # Ask the user to select where to save the PDF
    pdf_file_path = filedialog.asksaveasfilename(
        title="Save PDF File",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_file_path:
        return  # If no save location is specified, exit early

    try:
        # Convert the selected PowerPoint file to PDF
        pptxtopdf.convert(ppt_file_path, pdf_file_path)

        # Notify the user that the PDF was created successfully
        messagebox.showinfo("Success", f"PDF file created at: {pdf_file_path}")

    except Exception as e:
        # If there's an error, show a message with the error details
        messagebox.showerror("Error", f"Error converting PowerPoint to PDF: {str(e)}")

# Create the GUI window
root = tk.Tk()
root.title("PowerPoint to PDF Converter")

# Create a button to start the conversion process
convert_button = tk.Button(root, text="Convert PPT/PPTX to PDF", command=convert_to_pdf)
convert_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
