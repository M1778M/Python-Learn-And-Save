import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(900,900)
        label=QLabel("PYQT5")
        label2=QLabel("Faradars")
        button=QPushButton("button")
        tabwidget=QTabWidget()
        layout.addWidget(tabwidget)
        tabwidget.addTab(label,"Tab1")
        tabwidget.addTab(label2,"Tab2")
        tabwidget.addTab(button,"Tab Button")
        button.setGeometry(QRect(200,200,200,200))
        button.setMaximumWidth(200)
        tabwidget.setTabsClosable(True)
        tabwidget.setMovable(True)
        tabwidget.setTabPosition(QTabWidget.South)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
