from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        global stackedwidget
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(700,600)
        stackedwidget=QStackedWidget()
        layout.addChildWidget(stackedwidget)
        stackedwidget.setGeometry(QRect(400,200,200,200))
        label=QLabel("Faradars (PYQT5)")
        stackedwidget.addWidget(label)
        label2=QLabel("Settings")
        stackedwidget.addWidget(label2)
        label3=QLabel("Exit")
        stackedwidget.addWidget(label3)
        button=QPushButton("Main")
        button2=QPushButton("Setting")
        button3=QPushButton("Exit")
        layout.addChildWidget(button)
        layout.addChildWidget(button2)
        layout.addChildWidget(button3)
        button.setGeometry(QRect(30,100,100,100))
        button2.setGeometry(QRect(30,250,100,100))
        button3.setGeometry(QRect(30,400,100,100))
        button.clicked.connect(self.on_click1)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)
    def on_click1(self):
        stackedwidget.setCurrentIndex(0)
    def on_click2(self):
        stackedwidget.setCurrentIndex(1)
    def on_click3(self):
        stackedwidget.setCurrentIndex(2)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
