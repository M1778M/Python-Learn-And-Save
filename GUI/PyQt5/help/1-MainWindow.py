#----------SetWindow--------------
# screen.setTitle(str("title"))
# screen.resize(int(x),int(y))
# screen.setWidth(int(width))
# screen.setHeight(int(height))
# screen.setMinimumWidth(int(width))
# screen.setMinimumHeight(int(height))
# screen.setMaximumWidth(int(width))
# screen.setMaximumHeight(int(height))
#--------------------------------
#--------------Show--------------
# screen.showMinimized()
# screen.showMaximized()
# screen.showFullScreen()
#--------------------------------
#------------QLabel--------------
# label = QLabel()
# label.setText(str(text))
# label.text()
# label.setWordWrap(bool(true or false))
# label.setMargin(int(margin))
# label.setIndent(int(indent))
# label.setAlignment(Below)
#       Qt.AlingLeft
#       Qt.AlingHCenter
#       Qt.AlingRight
#       Qt.AlingJustify
#       Qt.AlingTop
#       Qt.AlingVCenter
#       Qt.AlingBottom
#       Qt.AlingBaseline
#------------QBoxLayout----------
# layout = QBoxLayout(QBoxLayout.LeftToRight)
# layout.addWidget(widget.int(stretch),aligment)
# layout.inserWidget(int(index),widget,int(stretch),aligment)
#--------------------------------
#------------QGridLayout---------
# layout = QGridLayout()
# layout.addWidget(widget,int(row),int(column),int(rowspan),int(columnspan),aligment)
# layout.setHorizontalSpacing(int(spacing))
# layout.setVerticalSpacing(int(spacing))
# 
#App

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from time import sleep

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,450)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        label = QLabel('label_1')
        layout.addWidget(label,0,Qt.AlignCenter)
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        label = QLabel('label_2')
        layout2.addWidget(label)
        label = QLabel('label_3')
        layout2.addWidget(label)
class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,450)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel('label_1 spacing 2 columns')
        layout.addWidget(label,0,0,0,2)
        label = QLabel('label_2 spacing 2 rows')
        layout.addWidget(label,2,0,2,0)
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
app2 = QApplication(sys.argv)
screen2 = Window2()
screen2.show()
#sleep(2)
#screen.setMinimumWidth(800)
sys.exit(app.exec_() and app2.exec_())