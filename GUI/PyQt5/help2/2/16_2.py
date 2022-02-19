from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        global calnendar
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(700,700)
        calnendar=QCalendarWidget()
        layout.addChildWidget(calnendar)
        calnendar.setGeometry(QRect(100,200,400,400))
        button=QPushButton("button")
        layout.addChildWidget(button)
        button.setGeometry(QRect(50,40,80,80))
        button.clicked.connect(self.on_click)
    def on_click(self):
        calnendar.showNextYear()
        print(calnendar.selectedDate())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
