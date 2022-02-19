from PyQt5.QtWidgets import *
from PyQt5.Qt import QApplication
import sys
class window(QWidget):
    def __init__(self):
        global label,clipboard
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        clipboard=QApplication.clipboard()
        clipboard.setText("Faradars")
        label=QLabel("text")
        layout.addWidget(label)
        clipboard.dataChanged.connect(self.clipboard)
        label.setStyleSheet("color: red")
    def clipboard(self):
        label.setText(clipboard.text())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
