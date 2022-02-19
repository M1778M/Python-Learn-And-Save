from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        lcdnumber=QLCDNumber()
        layout.addWidget(lcdnumber)
        lcdnumber.display(15)
        lcdnumber.setHexMode()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
