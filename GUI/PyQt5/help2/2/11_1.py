from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        toolbar=QToolBar()
        layout.addWidget(toolbar)
        toolbutton1=QToolButton()
        toolbutton1.setText("button1")
        toolbutton1.setCheckable(True)
        toolbar.addWidget(toolbutton1)
        toolbutton2=QToolButton()
        toolbutton2.setText("button2")
        toolbutton2.setCheckable(True)
        toolbar.addWidget(toolbutton2)
        toolbar.setOrientation(Qt.Vertical)
        toolbar.addSeparator()
        button=QPushButton("push button")
        layout.addWidget(button)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
