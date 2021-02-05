import os
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QVBoxLayout
from time import sleep
from PyQt5 import uic,QtCore

form1 = uic.loadUiType(os.path.join(os.getcwd(), "form.ui"))[0]
form2 = uic.loadUiType(os.path.join(os.getcwd(), "form2.ui"))[0]
class IntroWindow2(QMainWindow,form2):

    def __init__(self):
        super(IntroWindow2, self).__init__()
        self.setupUi(self)
        self.NextButton.clicked.connect(self.close)
 
class IntroWindow1(QMainWindow,form1):
    def __init__(self):
        super(IntroWindow1, self).__init__()
        self.setupUi(self)
 
        self.CreatButton.clicked.connect(self.create)
    def create(self):
        self.t=IntroWindow2()
        self.t.show()
        self.close()
 
 
 
    
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = IntroWindow1()
    main.show()
    sys.exit(app.exec_())