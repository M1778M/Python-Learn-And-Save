#!
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip
from PyQt5 import QtCore
class window(QWidget):
    def __init__(self):
        super(window,self).__init__()
        self.initMe()
    def initMe(self):
        self.setGeometry(100,100,500,500)



app = QApplication([])
w = window()

w.setWindowTitle("JAVA")

button = QPushButton("NameBTN")

button.move(100,100)

button.show()
w.show()

exit(app.exec_())