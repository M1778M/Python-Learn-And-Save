from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
count=0
class window(QWidget):
    def __init__(self):
        global count,pb,pd
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(700,700)
        spaceritem=QSpacerItem(100,100)
        layout.addItem(spaceritem,0,1)
        pb=QProgressBar()
        layout.addWidget(pb,0,0)
        pb.setMinimum(0)
        pb.setMaximum(100)
        pb.setValue(0)
        pb.setOrientation(Qt.Horizontal)
        pb.setTextVisible(True)
        buttonadd=QPushButton("add")
        layout.addWidget(buttonadd)
        buttonadd.clicked.connect(self.add)
        buttonexit=QPushButton("exit")
        layout.addWidget(buttonexit)
        buttonexit.clicked.connect(self.exitbutton)
        pd=QProgressDialog()
        layout.addWidget(pd)
        pd.setMinimum(0)
        pd.setMaximum(100)
        pd.setValue(0)
    def add(self):
        global count
        count=count+1
        pd.setValue(count)
        pb.setValue(count)
        if pd.wasCanceled()==True:
            print("canceled")
    def  exitbutton(self):
        exit()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
