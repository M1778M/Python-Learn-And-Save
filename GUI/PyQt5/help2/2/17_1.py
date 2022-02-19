from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        dateedit=QDateEdit()
        dateedit.setDate(QDate.currentDate())
        d=(dateedit.date().toString("yyyy.MM.dd"))
        dateedit.setMinimumDate(QDate(2019,12,25))
        dateedit.setMaximumDate(QDate(2020,12,28))
        label=QLabel("label")
        label.setText(d)
        layout.addWidget(label)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
