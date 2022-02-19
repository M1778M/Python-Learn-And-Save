from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        global listwidget,label
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(700,500)
        button=QPushButton("show list")
        layout.addWidget(button)
        button.clicked.connect(self.buttonclicked)
        label=QLabel("label")
        layout.addWidget(label)
        listwidget=QListWidget()
        listwidget.insertItem(0,"python")
        listwidget.insertItem(1,"c++")
        listwidget.insertItem(2,"java")
        listwidget.insertItem(3,"php")
        listwidget.insertItem(4,"c")
        layout.addWidget(listwidget)
        listwidget.clicked.connect(self.listwidgetclicked)
        listwidget.hide()
        listwidget.sortItems(Qt.AscendingOrder)
    def buttonclicked(self):
        listwidget.show()
    def listwidgetclicked(self):
        item=listwidget.currentItem()
        label.setText("Selected: "+(item.text())+"  row: "+str(listwidget.currentRow()))
        print(item.text())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
