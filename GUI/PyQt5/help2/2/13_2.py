import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.resize(900,600)
        self.setLayout(layout)
        tabbar=QTabBar()
        tabbar.addTab("Tab 1")
        tabbar.addTab("Tab 2")
        tabbar.addTab("Tab 3")
        tabbar.addTab("button")
        layout.addChildWidget(tabbar)
        tabbar.setGeometry(QRect(50,50,350,50))
        tabbar.setMovable(True)
        tabbar.setTabsClosable(True)
        button=QPushButton("button")
        layout.addChildWidget(button)
        button.setGeometry(QRect(200,150,170,80))
        button.clicked.connect(self.on_click)
    def on_click(self):
        exit()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
