from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        time=QTime()
        time.setHMS(18,22,00)
        timeedit=QTimeEdit()
        timeedit.setTime(time)
        layout.addWidget(timeedit)
        timeedit.setMinimumTime(QTime(18,21,00))
        timeedit.setMaximumTime(QTime(18,40,25))
        dt=QDateTime.currentDateTime()
        label=QLabel(dt.toString())
        layout.addWidget(label)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
