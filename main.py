import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QFormLayout
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from fpdf import FPDF, HTMLMixin


form = uic.loadUiType(os.path.join(os.getcwd(), "form.ui"))[0]
form2 = uic.loadUiType(os.path.join(os.getcwd(), "form2.ui"))[0]
form3 = uic.loadUiType(os.path.join(os.getcwd(), "form3.ui"))[0]
       
class HTML2PDF(FPDF, HTMLMixin):
        pass

class IntroWindow3(QMainWindow,form3):  
    def __init__(self):
        super(IntroWindow3, self).__init__()
        self.setupUi(self)
        self.CreateButton.clicked.connect(self.create)
        self.ExitButton.clicked.connect(lambda: self.close())
    def create(self):
        self.t=IntroWindow()
        self.t.show()
        self.close()

class IntroWindow2(QMainWindow,form2):  
    def __init__(self):
        super(IntroWindow2, self).__init__()
        self.setupUi(self)
        self.DoneButton.clicked.connect(lambda: self.close())

class IntroWindow(QMainWindow, form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)
        self.PrintButton.clicked.connect(self.html2pdf)
        self.QuitButton.clicked.connect(self.exit)
        self.PrintButton.clicked.connect(self.create)
    def create(self):
        self.t=IntroWindow2()
        self.t.show()


        
        
    def exit(self):
        app.quit()  


    def html2pdf(self ):
        
        Name = self.nameLineEdit.text()
        email = self.emailLineEdit.text()
        address = self.addressLineEdit.text()
        phone = self.phoneLineEdit.text()
        education = self.educationLineEdit.text()
        experience1 = self.experience1LineEdit.text()
        experience2 = self.experience2LineEdit.text()
        experience3 = self.experience3LineEdit.text()
        nCAP = self.nCAPLineEdit.text()
        lan = self.languagesLineEdit.text()
        intrests = self.hobbiesLineEdit.text()
        about = self.descriptionLineEdit.text()
        job = self.jobLineEdit.text()
        skills = self.skillsLineEdit.text()
        refrences = self.refrencesLineEdit.text()
        
        html = f'''<!DOCTYPE html>
        <html>
        <head>
        <style>
        
        </style>
        </head>
        <div id="header"></div>
        <div class="left"></div>
        <div class="stuff">
        <br><br>
        <h1>Resume</h1>
        <h2>{Name}</h2>
        <hr />
        <br>
        <p class="head">Interests</p>
        <ul>
            <li>{intrests}</li>
        </ul>
        <p class="head">Skills</p>
        <ul>
            <li>{skills}</li>
        </ul>
        <p class="head">Education</p>
        <ul>
            <li>{education}</li>
        </ul>
        <p class="head">Experience</p>
        <ul>
            <li>{experience1}</li>
            <li>{experience2}</li>
            <li>{experience3}</li>
        </ul>
        <p class="head">Notable </p>
        <ul>
            <li>Recycling Club</li>
            <li>Gardening Club</li>
            <li>Book Club</li>
        </ul>
        </div>
        <div class="right"></div>
        <div id="footer">
        <h2 id="name">Emily</h2></div>

    '''

        pdf = HTML2PDF()
        #First page
        pdf.add_page()
        pdf.write_html(html)
        pdf.output('Resume.pdf', 'F')

    
    






       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow3()
    w.show()
    sys.exit(app.exec_())
