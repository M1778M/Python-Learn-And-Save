from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class window(QWidget):
    def __init__(self):
        global frame
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(400,500)
        button=QPushButton("click me")
        layout.addWidget(button)
        button.clicked.connect(self.buttonclick)
        frame=QFrame()
        layout.addWidget(frame)
        frame.setLineWidth(50)
        frame.setFrameShape(QFrame.WinPanel)
        frame.setStyleSheet("background-color:pink;")
    def buttonclick(self):
        frame.setStyleSheet("background-image: url(ball.jpg);")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
