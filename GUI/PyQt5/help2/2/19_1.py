from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class window(QWidget):
    def __init__(self):
        global label
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        label=QLabel("Python")
        layout.addChildWidget(label)
        label.setGeometry(QRect(50,50,400,300))
        label.setFont(QFont("Arial",30))
        button=QPushButton("Open Fonts")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
    def on_click(self):
        getfont,ok=QFontDialog.getFont()
        if ok:
            label.setFont(getfont)
            print(getfont.toString())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
