import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyPDF2 import PdfReader, PdfWriter
import os

class PDFTool(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.page_range_label = QLabel('Enter page range (e.g., 1-5):', self)
        self.page_range_input = QLineEdit(self)
        self.split_button = QPushButton('Split PDF', self)
        self.split_button.clicked.connect(self.split_pdf)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.page_range_label)
        layout.addWidget(self.page_range_input)
        layout.addWidget(self.split_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Window settings
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle('PDF Tool')

    def split_pdf(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Open PDF File', '', 'PDF Files (*.pdf)')
            if file_path:
                page_range = self.page_range_input.text()
                start_page, end_page = map(int, page_range.split('-'))

                pdf_reader = PdfReader(file_path)
                pdf_writer = PdfWriter()

                for page_num in range(start_page - 1, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                output_dir = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')
                if output_dir:
                    output_file = os.path.join(output_dir, f'split_pages_{start_page}-{end_page}.pdf')
                    with open(output_file, 'wb') as output:
                        pdf_writer.write(output)

                print('PDF Split Successful!')
        except Exception as e:
            print(f"Error during PDF split: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_tool = PDFTool()
    pdf_tool.show()
    sys.exit(app.exec_())
