#--------QPushButton--------
# btn = QPushButton()
# btn.setText(str(label))
# btn.setFlat(bool(true or false))
# btn.clicked.connect(func)
# btn.setIcon(QtGui.QIcon(file))
#---------------------------
#----------QRadioButton------
# rdb = QRadioButton()
# rdb.setText(str(label))
# rdb.setChecked(bool(true or false))
# rdb.isChecked()
# rdb.setIcon(QtGui.QIcon(file))
# rdb.toggled.connect(self.ifClicked)
#---------------------------------
#-------------QCheckBox-----------
# checkbox = QCheckBox()
# checkbox.setText(str(label))
# checkbox.setChecked(bool(true or false))
# checkbox.isChecked()
# checkbox.setTristate(bool(true or false))
# checkbox.isTristate()
#-------------------------------
#------------ButtonGroup--------
# btng = QButtonGroup()
# btng.addButton(button, int(id))
# btng.removeButton(button)
# btng.id(button)
# btng.setId(button, int(id))
#-------------------------------
#----------QGroupBox-------------
# grb = QGroupBox()
# grb.setTitle(str(title))
# grb.setCheckable(bool(true or false))
# grb.setChecked()
# grb.setAlingnment(alignment)
#            Qt.AlingLeft
#            Qt.AlingRight
#            Qt.AlingHCenter
#---------------------------
#--------QSizeGrip----------
# sizegrip = QSizeGrip(parent)
# sizegrip.setVisible(bool(true or false))


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,500)
        btn = QPushButton("BTN_1")
        layout.addWidget(btn)
        btn.setIcon(QtGui.QIcon('Data\\btn_.ico'))
        btn.clicked.connect(self.ifClicked)
    def ifClicked(self):
        print('Button Clicked')

class window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,500)
        btn = QRadioButton('Button_1')
        layout.addWidget(btn)
        btn.toggled.connect(self.rdb1Clicked)
        btn2 = QRadioButton('Button_2')
        layout.addWidget(btn2)
        btn2.toggled.connect(self.rdb2Clicked)
    def rdb1Clicked(self):
        print('QRadioButton 1 Clicked')
        btn=self.sender()
        if btn.isChecked():
            print('QRadioButton 1 selected')
    def rdb2Clicked(self):
        print('QRadioButton 2 Clicker')
        btn2=self.sender()
        if btn2.isChecked():
            print('QRadioButton 2 selected')
class window3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        self.cb1 = QCheckBox('checkbox_1')
        self.cb1.setChecked(True)
        layout.addWidget(self.cb1)
        self.cb1.toggled.connect(self.CheckTheBox)
        self.cb2 = QCheckBox('checkbox_2')
        layout.addWidget(self.cb2)
        self.cb2.toggled.connect(self.CheckTheBox)
        self.cb2.setTristate(True)
    def CheckTheBox(self):
        if self.cb1.isChecked():
            print('checkBox_1 clicked')
        if self.cb2.isChecked():
            print('checkBox_2 clicked')
        
class window4(QWidget):
    def __init__(self):
        global btng
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,650)
        btn = QPushButton('btn 1')
        layout.addWidget(btn)
        btn2 = QPushButton('btn 2')
        layout.addWidget(btn2)
        btn3 = QPushButton('btn 3')
        layout.addWidget(btn3)
        btng = QButtonGroup()
        btng.addButton(btn,1)
        btng.addButton(btn2,2)
        btng.addButton(btn3,3)
        btng.buttonClicked[int].connect(self.BTNCLICK)
    def BTNCLICK(self,Id):
        print('number %s clicked' % Id)

class window5(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,650)
        box = QGroupBox('group Box')
        layout.addWidget(box)
        box.setCheckable(True)
        sublayout = QGridLayout()
        box.setLayout(sublayout)
        btn = QPushButton('btn1')
        sublayout.addWidget(btn)
        btn2 = QPushButton('btn2')
        sublayout.addWidget(btn2)


        
app = QApplication(sys.argv)
screen = window()
screen.show()
app2 = QApplication(sys.argv)
screen2 = window2()
screen2.show()
app3 = QApplication(sys.argv)
screen3 = window3()
screen3.show()
app4 = QApplication(sys.argv)
screen4 = window4()
screen4.show()
app5 = QApplication(sys.argv)
screen5 = window5()
screen5.show()


sys.exit(app.exec_() and app2.exec_() and app3.exec_() and app4.exec_() and app5.exec_())