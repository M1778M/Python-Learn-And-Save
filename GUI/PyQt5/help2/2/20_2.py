from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        global tablewidget
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        tablewidget=QTableWidget()
        layout.addWidget(tablewidget)
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        tablewidget.setColumnWidth(3,200)
        tablewidget.setRowHeight(3,200)
        button=QPushButton("Calculate")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
        tablewidget.setShowGrid(False)
        tablewidget.setEditTriggers(QAbstractItemView.DoubleClicked)
    def on_click(self):
        s1=tablewidget.item(0,0).text()
        s2=tablewidget.item(1,0).text()
        s3=tablewidget.item(2,0).text()
        tablewidget.setItem(3,0,QTableWidgetItem(" sum: "+str(int(s1)+int(s2)+int(s3))))
        tablewidget.setItem(3,1,QTableWidgetItem(" sub: "+str(-int(s1)-int(s2)-int(s3))))
        tablewidget.setItem(3,2,QTableWidgetItem(" mul: "+str(int(s1)*int(s2)*int(s3))))
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
