#-------------QSplitter-----------
# splitter=QSplitter()
# splitter.addWidget(widget)
# splitter.count()
# splitter.setHandleWidth(int(width))
# splitter.setOrientation(orientation)
#           Qt.Horizontal
#           Qt.Vertical
#-----------------------------------
#-----------QFrame------------------
# frame = QFrame()
# frame.setLineWidth(int(width))
# frame.setFrameShadow(shadow)
#               QFrame.Plain
#               QFrame.Raised
#               QFrame.Sunken
# frame.setFrameShape(shape)
#               QFrame.NoFrame
#               QFrame.Box
#               QFrame.Panel
#               QFrame.StyledPanel
#               QFrame.HLine
#               QFrame.VLine
#               QFrame.WinPanel
#------------------------------------
#--------------QSlider---------------
# slider = QSlider(orientation)
# slider.setOrientation(orientation)
#           Qt.Horizontal
#           Qt.Vertical
# slider.setValue(int(value))
# slider.value()
# slider.setTickPosition(position)
#           QSlider.NoTicks
#           QSlider.TicksBothSides
#           QSlider.TicksAbove
#           QSlider.TicksBelow
#           QSlider.TicksLeft
#           QSlider.TicksRight
# slider.setMinimum(int(value))
# slider.setMaximum(int(value))
#-------------------------------
#-----------QScrollBar----------
# scb = QScrollBar()
# scb = QScrollBar(orientation)
#               Qt.Horizontal
#               Qt.Vertical
#-------------------------------
#----------QScrollArea----------
# sca = QScrollArea()
# sca.setWidget(widget)
# sca.setWidgetResizable(bool(true or false))
# sca.setAlignment(alignment)
#               Qt.AlignLeft
#               Qt.AlignRight
#               Qt.AlignTop
#               Qt.AlignHCenter
#               Qt.AlignBottom
#               Qt.AlignVCenter
#----------------------------------
#--------------QSpinBox------------
# spinbox = QSpinBox()
# spinbox.setValue(int(value))
# spinbox.setRange(int(minimum), int(maximum))
# spinbox.setPrefix(str(prefix))
# spinbox.setSuffix(str(suffix))
# spinbox.setSingleStep(int(value))
# spinbox.valueChanged->
# spinbox.valueChanged.connect()
#------------------------------
#---------QDoubleSpinBox-------
# dsb = QDoubleSpinBox()
# dsb.setValue(int(value))
# dsb.setRange(int(minimum), int(maximum))
# dsb.setPrefix(str(prefix))
# dsb.setSuffix(str(suffix))
# dsb.setSingleStep(int(value))
# dsb.valueChanged->
# dsb.valueChanged.connect()
#------------------------------
#-------------QDial------------
# dial = QDial()
# dial.setValue(int(value))
# dial.setWrapping(bool(true or false))
# dial.setMinimum(int(minimum))
# dial.setMaximum(int(maximum))
# dial.valueChanged->
# dial.valueChanged.connect()
#--------------------------------
#------------QLcdNumber----------
# lcdn = QLcdNumber()
# lcdn.display(int(num)) #-> setValue0
# lcdn.value()
# lcdn.setSmallDecimalPoint(bool(true or false))
# lcdn.setMode(mode)
#           Bin -> lcdn.setBinMode()
#           Oct -> lcdn.setOctMode()
#           Dec (default)
#           Hex -> lcdn.setHexMode()
#-----------------------------------
#--------------QSpacerItem----------
# spi = QSpacerItem(int(x), int(y))
# layout.addItem(spi)
#-----------------------------------
#--------------QProgressBar---------
# prossbar = QProgressBar()
# prossbar.setMinimum(int(minimum))
# prossbar.setMaximum(int(maximum))
# prossbar.setValue(int(value))
# prossbar.value()
# prossbar.setInvertedAppearance(bool(true or false))
# prossbar.setTextVisible(bool(true or false))
# prossbar.setFormat(("%v") or ("%m"))
# prossbar.resetFormat()
# prossbar.setOrientation(orientation)
#                       Qt.Horizontal
#                       Qt.Vertical
#----------------------------------------
#----------------QProgressDialog---------
# prosslog = QProgressDialog()
# prosslog.setMinimum(int(minimum))
# prosslog.setMaximum(int(maximum))
# prosslog.setValue(int(value))
# prosslog.value()
# prosslog.setCancelButton(widget)
# prosslog.wasCanceled()
# 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        btn = QPushButton('Button_1')
        btn2 = QPushButton('Button_2')
        btn3 = QPushButton('Button_3')
        splitter = QSplitter()
        layout.addWidget(splitter)
        splitter.addWidget(btn)
        splitter.addWidget(btn2)
        splitter.addWidget(btn3)
        splitter.setOrientation(Qt.Vertical)
        splitter.setHandleWidth(50)
        s = splitter.count()
        print(s)

class window2(QWidget):
    def __init__(self):
        global frame
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(400,500)
        btn = QPushButton('clickMe')
        layout.addWidget(btn)
        btn.clicked.connect(self.btnClick)
        frame = QFrame()
        layout.addWidget(frame)
        frame.setLineWidth(50)
        frame.setFrameShape(QFrame.WinPanel)
        frame.setStyleSheet('background-color:pink;')
    def btnClick(self):
        frame.setStyleSheet('background-image: url(\'Data/btn_.ico\');')
        
class window3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(4)
        layout.addWidget(self.slider,0,0)
        self.slider2 = QSlider(Qt.Vertical)
        self.slider2.setValue(4)
        self.slider2.setTickPosition(QSlider.TicksBothSides)
        layout.addWidget(self.slider2,0,1)
        self.label = QLabel('label')
        layout.addWidget(self.label)
        self.btn = QPushButton('slider1 Value')
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.btnclick)
    def btnclick(self):
        self.label.setText(str(self.slider.value()))

class window4(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,600)
        scb = QScrollBar(Qt.Vertical)
        layout.addWidget(scb)
        sca = QScrollArea()
        layout.addWidget(sca)
        sca.setAlignment(Qt.AlignTop)
        label = QLabel('aaaaaaasssssssdsafsdgsdgdrgerk;gkerpogkjreiogjkpoekjgo;ro;gjdrogjl;djglodfjgoldrjgporejopjgepojgpergjoerijgoierjgioerjgoierjgoirejoigerjogjerogjeorigjoiergjoierjgiorjgo')
        sca.setWidget(label)
        
class window5(QWidget):
    def __init__(self):
        global spinbox
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        spinbox = QSpinBox()
        layout.addWidget(spinbox)
        spinbox.setRange(0,100)
        spinbox.setPrefix('value ')
        spinbox.setSuffix(' cm')
        spinbox.setSingleStep(2.5)
        spinbox.valueChanged.connect(self.vlCh)
    def vlCh(self):
        print(spinbox.value())

class window6(QWidget):
    def __init__(self):
        global dsb
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        dsb = QDoubleSpinBox()
        layout.addWidget(dsb)
        dsb.setRange(0,1)
        dsb.setPrefix('Value ')
        dsb.setSuffix(' cm')
        dsb.setSingleStep(0.01)
        dsb.valueChanged.connect(self.dsbCh)
    def dsbCh(self):
        print(dsb.value())

class window7(QWidget):
    def __init__(self):
        global dial, label
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        dial = QDial()
        layout.addWidget(dial)
        dial.setMinimum(0)
        dial.setMaximum(100)
        dial.setValue(0)
        dial.valueChanged.connect(self.dialCh)
        label = QLabel('label')
        layout.addWidget(label)
    def dialCh(self):
        print(dial.value())
        label.setText(str(dial.value()))

class window8(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        lcdn = QLCDNumber()
        layout.addWidget(lcdn)
        lcdn.display(15)
        lcdn.setBinMode()
        
count = 0
class window9(QWidget):
    def __init__(self):
        global count, pb,pd
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(700,700)
        spaceritem = QSpacerItem(100,200)
        layout.addItem(spaceritem,0,1)
        pb = QProgressBar()
        layout.addWidget(pb,0,0)
        pb.setMinimum(0)
        pb.setMaximum(100)
        pb.setValue(0)
        pb.setOrientation(Qt.Horizontal)
        pb.setTextVisible(True)
        btnAdd = QPushButton('add')
        layout.addWidget(btnAdd)
        btnAdd.clicked.connect(self.add)
        btnExit=QPushButton('Exit')
        layout.addWidget(btnExit)
        btnExit.clicked.connect(self.exbt)
        pd = QProgressDialog()
        layout.addWidget(pd)
        pd.setMinimum(0)
        pd.setMaximum(100)
        pd.setValue(0)
    def add(self):
        global count
        count+=1
        pd.setValue(count)
        pb.setValue(count)
        if pd.wasCanceled()==True:
            print('canceled')
    def exbt(self):
        exit()

app = QApplication(sys.argv)
screen=window()
screen.show()
app2 = QApplication(sys.argv)
screen2=window2()
screen2.show()
app3 = QApplication(sys.argv)
screen3=window3()
screen3.show()
app4 = QApplication(sys.argv)
screen4=window4()
screen4.show()
app5 = QApplication(sys.argv)
screen5=window5()
screen5.show()
app6 = QApplication(sys.argv)
screen6=window6()
screen6.show()
app7 = QApplication(sys.argv)
screen7=window7()
screen7.show()
app8 = QApplication(sys.argv)
screen8=window8()
screen8.show()
app9 = QApplication(sys.argv)
screen9=window9()
screen9.show()


sys.exit(app.exec_() and app2.exec_() and app3.exec_() and app4.exec_() and app5.exec_() and app6.exec_() and app7.exec_() and app8.exe_() and app9.exe_())