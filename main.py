import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

w = QWidget()
w.resize(1500, 1500)
w.move(300, 300)
w.setWindowTitle("Resume Builder")

def btn_callback():
    print("Quit..")
    app.quit()


b = QPushButton("Quit", w)
b.resize(200, 100)
b.move(650, 1300)
b.clicked.connect(btn_callback)



w.show()

sys.exit(app.exec_())