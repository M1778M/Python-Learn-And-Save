from PyQt5.QtWidgets import *
import  sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QFormLayout()
        self.setLayout(layout)
        self.resize(600,600)
        button=QPushButton("button 1")
        layout.addRow("formlayout",button)
        layout.setHorizontalSpacing(200)
        layout.setVerticalSpacing(200)
        button2=QPushButton("button 2")
        layout.insertRow(2,"formlayout2",button2)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
