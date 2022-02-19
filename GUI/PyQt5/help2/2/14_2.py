from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        dockwidget=QDockWidget()
        layout.addWidget(dockwidget)
        button=QPushButton("button 1")
        dockwidget.setWidget(button)
        dockwidget2=QDockWidget()
        layout.addWidget(dockwidget2)
        button2=QPushButton("button 2")
        dockwidget2.setWidget(button2)
        label=QLabel("Faradars")
        dockwidget.setTitleBarWidget(label)
        dockwidget2.setWindowTitle("This is a pushbutton")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
