from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(500,500)
        layout=QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        label=QLabel("label 1")
        layout.addWidget(label,0,Qt.AlignCenter)
        layout2=QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        label=QLabel("label 2")
        layout2.addWidget(label)
        label=QLabel("label 3")
        layout2.addWidget(label)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
