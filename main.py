import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QFormLayout,QLabel,QLineEdit,QPushButton, QComboBox
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from fpdf import FPDF, HTMLMixin
from xhtml2pdf import pisa             # import python module
from flask import Flask


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

    # Utility function
    def convert_html_to_pdf(self, source_html, output_filename):
        # open output file for writing (truncated binary)
        result_file = open(output_filename, "w+b")

        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(
                source_html,                # the HTML to convert
                dest=result_file)           # file handle to recieve result
        # close output file
        result_file.close()                 # close output file
        # return False on success and True on errors
        return pisa_status.err    
        
    def html2pdf(self ):
        
        Name = self.nameLineEdit.text()
        lastname = self.lastnameLineEdit.text()
        email = self.emailLineEdit.text()
        address = self.addressLineEdit.text()
        phone = self.phoneLineEdit.text()
        education = self.educationLineEdit.text()
        experience1 = self.experience1LineEdit.text()
        experience2 = self.experience2LineEdit.text()
        experience3 = self.experience3LineEdit.text()
        nCAP = self.nCAPLineEdit.text()
        interests = self.hobbiesLineEdit.text()
        about = self.descriptionLineEdit.text()
        job = self.jobLineEdit.text()
        skills = self.skillsLineEdit.text()
        layout = self.layoutColorComboBox.currentText()

        html = ""

        
        simple_pink = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
        <html style="max-width: 700px;
        margin: auto;"><body style="max-width: 700px;
        margin: auto;">
        <div id="header" style="max-width:700px;margin:auto;border-radius:5px;height:40px;width:100%;background-color:#ffcccc;position:fixed;z-index:1;"></div>
        
        <div class="stuff" style="max-width:700px;margin:auto;border-radius:5px;display:inline-block;margin-top:6px;margin-left:10px;width:100%;height:1000px;">
        <br style="max-width: 700px;
        margin: auto;"><br style="max-width: 700px;
        margin: auto;"><h1 style="max-width: 700px;
        margin: auto;">Resume</h1>
        <h2 style="max-width: 700px;
        margin: auto;">{Name} {lastname} </h2>
        <hr style="max-width: 700px;
        margin: auto;">
        <br style="max-width: 700px;
        margin: auto;"><p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Interests</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{interests}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Skills</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{skills}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Education</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <a style="max-width:700px;margin:auto;color:black;text-decoration:none;">
            <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{education}</li>
            </a>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Experience</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience1}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience2}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience3}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">About me</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{job} | {about}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Notable Courses and Projects</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{nCAP}</li>
        </ul>
        </div>
        
        <div id="footer" style="max-width:700px;margin:auto;border-radius:5px;height:50px;width:100%;background-color:#ffcccc;clear:both;position:relative;">
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{phone} | {email}</h2>
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{address}</h2>
        </div>
        </body></html>
            '''
        simple_green = f'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
        <html style="max-width: 700px;
        margin: auto;"><body style="max-width: 700px;
        margin: auto;">
        <div id="header" style="max-width:700px;margin:auto;border-radius:5px;height:40px;width:100%;background-color:#28B463 ;position:fixed;z-index:1;"></div>
        
        <div class="stuff" style="max-width:700px;margin:auto;border-radius:5px;display:inline-block;margin-top:6px;margin-left:10px;width:100%;height:1000px;">
        <br style="max-width: 700px;
        margin: auto;"><br style="max-width: 700px;
        margin: auto;"><h1 style="max-width: 700px;
        margin: auto;">Resume</h1>
        <h2 style="max-width: 700px;
        margin: auto;">{Name} {lastname} </h2>
        <hr style="max-width: 700px;
        margin: auto;">
        <br style="max-width: 700px;
        margin: auto;"><p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Interests</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{interests}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Skills</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{skills}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Education</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <a style="max-width:700px;margin:auto;color:black;text-decoration:none;">
            <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{education}</li>
            </a>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Experience</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience1}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience2}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience3}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">About me</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{job} | {about}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Notable Courses and Projects</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{nCAP}</li>
        </ul>
        </div>
        
        <div id="footer" style="max-width:700px;margin:auto;border-radius:5px;height:50px;width:100%;background-color:#28B463 ;clear:both;position:relative;">
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{phone} | {email}</h2>
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{address}</h2>
        </div>
        </body></html>
            '''    
        simple_blue= f'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
        <html style="max-width: 700px;
        margin: auto;"><body style="max-width: 700px;
        margin: auto;">
        <div id="header" style="max-width:700px;margin:auto;border-radius:5px;height:40px;width:100%;background-color:#FFBF00 ;position:fixed;z-index:1;"></div>
        
        <div class="stuff" style="max-width:700px;margin:auto;border-radius:5px;display:inline-block;margin-top:6px;margin-left:10px;width:100%;height:1000px;">
        <br style="max-width: 700px;
        margin: auto;"><br style="max-width: 700px;
        margin: auto;"><h1 style="max-width: 700px;
        margin: auto;">Resume</h1>
        <h2 style="max-width: 700px;
        margin: auto;">{Name} {lastname} </h2>
        <hr style="max-width: 700px;
        margin: auto;">
        <br style="max-width: 700px;
        margin: auto;"><p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Interests</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{interests}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Skills</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{skills}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Education</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <a style="max-width:700px;margin:auto;color:black;text-decoration:none;">
            <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{education}</li>
            </a>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Experience</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience1}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience2}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience3}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">About me</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{job} | {about}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Notable Courses and Projects</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{nCAP}</li>
        </ul>
        </div>
        
        <div id="footer" style="max-width:700px;margin:auto;border-radius:5px;height:50px;width:100%;background-color:#6495ED ;clear:both;position:relative;">
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{phone} | {email}</h2>
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{address}</h2>
        </div>
        </body></html>
            '''        

        simple_yellow= f'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
        <html style="max-width: 700px;
        margin: auto;"><body style="max-width: 700px;
        margin: auto;">
        <div id="header" style="max-width:700px;margin:auto;border-radius:5px;height:40px;width:100%;background-color:#6495ED ;position:relative;z-index:1;"></div>
        
        <div class="stuff" style="max-width:700px;margin:auto;border-radius:5px;display:inline-block;margin-top:6px;margin-left:10px;width:100%;height:1000px;">
        <br style="max-width: 700px;
        margin: auto;"><br style="max-width: 700px;
        margin: auto;"><h1 style="max-width: 700px;
        margin: auto;">Resume</h1>
        <h2 style="max-width: 700px;
        margin: auto;">{Name} {lastname} </h2>
        <hr style="max-width: 700px;
        margin: auto;">
        <br style="max-width: 700px;
        margin: auto;"><p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Interests</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{interests}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Skills</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{skills}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Education</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <a style="max-width:700px;margin:auto;color:black;text-decoration:none;">
            <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{education}</li>
            </a>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Experience</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience1}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience2}</li>
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{experience3}</li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">About me</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{job}|{about} </li>
        </ul>
        <p class="head" style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';font-size:20px;">Notable Courses and Projects</p>
        <ul style="max-width: 700px;
        margin: auto;">
        <li style="max-width:700px;margin:auto;font-family:'Cormorant Garamond';">{nCAP} </li>
        </ul>
        </div>
        
        <div id="footer" style="max-width:700px;margin:auto;border-radius:5px;height:50px;width:100%;background-color:#FFBF00 ;clear:both;position:relative;">
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{phone} | {email}</h2>
        <h2 id="name" style="max-width:700px;margin:auto;font-family:Sacramento;float:right;margin-top:10px;margin-right:4%;">{address}</h2>
        </div>
        </body></html>
            '''           

        if layout == "simple_pink":
            html = simple_pink
        elif layout == "simple_green":
            html = simple_green 
        elif layout == "simple_yellow" :
            html = simple_yellow
        else:
            html = simple_blue       


        output_filename = "Resume.pdf"
        pisa.showLogging()
        self.convert_html_to_pdf(html, output_filename)

    
    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow3()
    w.show()
    sys.exit(app.exec_())
