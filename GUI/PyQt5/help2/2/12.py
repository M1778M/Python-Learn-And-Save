from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class window(QWidget):
    def __init__(self):
        global label,label2
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        menubar=QMenuBar()
        layout.addWidget(menubar,0,0)
        new=menubar.addMenu("File")
        new.addAction("Create new file")
        new.triggered.connect(self.on_click)
        new.addSeparator()
        new.addAction("Create new project")
        new.addSeparator()
        new.addAction("Settings")
        new.addSeparator()
        new.addAction("exit")
        new2=menubar.addMenu("Help")
        newaction=QAction(QIcon("3.2.png"),"About us",self)
        newaction.setShortcut("Ctrl+N")
        newaction.triggered.connect(self.newcall)
        new2.addAction(newaction)
        label=QLabel("New file Created")
        layout.addWidget(label,2,0)
        label.hide()
        label2=QLabel("Fradars (PYQT5)")
        #layout.addWidget(label2)
        label2.hide()
    def on_click(self):
        label.show()
        print("ok")
    def newcall(self):
        label2.resize(300,300)
        label2.show()
        print("ok")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
