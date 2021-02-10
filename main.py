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

       
class HTML2PDF(FPDF, HTMLMixin):
        pass


class IntroWindow(QMainWindow, form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)
        self.PrintButton.clicked.connect(self.html2pdf)
        self.QuitButton.clicked.connect(self.exit)
        Name = self.nameLineEdit.text()
        email = self.emailLineEdit.text()
        education = self.educationLineEdit.text()
        experience = self.experienceLineEdit.text()
        nCAP = self.nCAPLineEdit.text()
        lan = self.languagesLineEdit.text()
        intrests = self.hobbiesLineEdit.text()
        about = self.descriptionLineEdit.text()
        job = self.jobLineEdit.text()


        
        
    def exit(self):
        app.quit()  


    def html2pdf(self ,Name= None, lastname= None, address= None, email= None, education= None, experience= None,nCAp= None, lan= None, intrests= None,about= None, job = None):
        html = ''' <div id="header"></div>
        <div class="left"></div>
        <div class="stuff">
        <br><br>
        <h1>Resume</h1>
        <h2>Emily</h2>
        <hr />
        <br>
        <p class="head">Interests</p>
        <ul>
            <li>{self.}</li>
            
        </ul>
        <p class="head">Skills</p>
        <ul>
            <li>Web Design with HTML & CSS</li>
        </ul>
        <p class="head">Education</p>
        <ul>
            <a href="http://www.wiltonhighschool.org/pages/Wilton_High_School">
            <li>Wilton High School</li>
            </a>
            <!--Link-->
            <a href="https://www.silvermineart.org/">
            <li>Silvermine School of Arts</li>
            </a>
            <li>Codeacademy</li>
        </ul>
        <p class="head">Experience</p>
        <ul>
            <li>Student Technology Intern for Wilton School District</li>
            <li>Babysitter</li>
        </ul>
        <p class="head">Extracurriculars</p>
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
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())
