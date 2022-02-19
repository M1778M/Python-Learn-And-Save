from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from time import sleep
value=0
class window(QWidget):
    def __init__(self):
        global gif,splashscreen,button,giflabel2,gif2,progress,value
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(1280,600)
        self.setStyleSheet("background-color: white;")
        splashscreen=QSplashScreen(QPixmap("small.jpg"))
        giflabel=QLabel()
        gif=QMovie("loadingbox.gif")
        giflabel.setMovie(gif)
        gif.start()
        layout.addChildWidget(giflabel)
        giflabel.setGeometry(QRect(200,100,600,300))
        giflabel2=QLabel()
        gif2=QMovie("last.gif")
        giflabel2.setMovie(gif2)
        gif2.stop()
        giflabel2.hide()
        layout.addChildWidget(giflabel2)
        giflabel2.setGeometry(QRect(200,10,800,500))
        layout.addWidget(splashscreen)
        progress=QProgressBar(splashscreen)
        progress.setGeometry(QRect(450,500,450,30))
        progress.setMaximum(10)
        splashscreen.hide()
        button=QPushButton("Start Windows")
        button.clicked.connect(self.click)
        button.setGeometry(QRect(520,400,300,100))
        layout.addChildWidget(button)
        button.setStyleSheet("background-color: blue;")
    def click(self):
        global value
        gif.stop()
        splashscreen.show()
        button.hide()
        while(value<11):
            sleep(1)
            value=value+1
            progress.setValue(value)
            app.processEvents()
        splashscreen.finish(self)
        giflabel2.show()
        gif2.start()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
