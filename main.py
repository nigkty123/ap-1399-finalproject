import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QFrame
from fpdf import FPDF
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter

form = uic.loadUiType(os.path.join(os.getcwd(), "form.ui"))[0]

class IntroWindow(QMainWindow, form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)
        self.textEdit = QTextEdit(self)
        self.PrintButton.clicked.connect(self.PrintPDF)
        self.QuitButton.clicked.connect(self.exit)
    def exit(self):
        app.quit()  
    def PrintPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'print', None, 'Pdf files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() =="" : fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)




title = '20000 Leagues Under the Seas'

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())
    pdf = PDF()
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
    pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
    pdf.output('tuto3.pdf', 'F')
