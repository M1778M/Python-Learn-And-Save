from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        toolbox=QToolBox()
        layout.addWidget(toolbox)
        label=QLabel()
        toolbox.addItem(label,QIcon("3.2.png"),"python")
        label=QLabel()
        toolbox.addItem(label,"C++")
        print(toolbox.count())
        toolbar=QToolBar()
        button=QPushButton("button1")
        toolbar.addWidget(button)
        button=QPushButton("button2")
        toolbar.addWidget(button)
        toolbox.insertItem(0,toolbar,"button")
        toolbutton=QToolButton()
        toolbutton.setText("faradars")
        toolbox.addItem(toolbutton,"toolbutton")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
