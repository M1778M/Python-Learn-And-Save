#------------QToolbar---------
# toolbar = QToolbar()
# toolbar.addWidget(widget)
# toolbar.addSeparator()
# toolbar.clear()
# toolbar.setOrientation(orientation)
#               Qt.Vertical
#               Qt.Horizontal
#--------------------------------------
#----------------QToolBox--------------
# toolbox = QToolBox()
# toolbox.addItem(child, str(label))
# toolbox.addItem(child,icon,str(label))
# toolbox.insertItem(index,child,str(label))
# toolbox.insertItem(index,child,icon,str(label))
# toolbox.removeItem(index)
# toolbox.currentIndex()
# toolbox.currentWidget()
# toolbox.count()
#----------------------------------------------
#------------QToolButton--------------------
# toolbtn = QToolButton()
# toolbtn.setText(str(text))
# toolbtn.setIcon(icon)
# toolbtn.setCheckable(bool(true or false))
# toolbtn.isChecked(checked)
# toolbtn.setDown(bool(true or false))


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Gui import *
import sys

class window(QWidget):  
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        toolbar = QToolBar()
        layout.addWidget(toolbar)
        toolbtn = QToolButton()
        toolbtn.setText('click')
        toolbtn.setCheckable(True)
        toolbar.addWidget(toolbtn)
        toolbtn2= QToolButton()
        toolbtn2.setText('click2')
        toolbtn2.setCheckable(True)
        toolbar.addWidget(toolbtn2)
        toolbar.setOrientation(Qt.Vertical)
        toolbar.addSeparator()
        btn = QPushButton('push btn')
        layout.addWidget(btn)

class window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        toolbox = QToolBox()
        layout.addWidget(toolbox)
        label = QLabel()
        toolbox.addItem(label,QIcon('data/btn_.ico'),'ToolBox')
        label = QLabel()
        toolbox.addItem(label,'ToolBoxAgain')
        print(toolbox.count())
        toolbar = QToolbar()
        btn = QPushButton('BTN1')
        toolbar.addWidget(btn)
        btn2 = QPushButton('BTN2'
        toolbar.addWidget(btn2))
        toolbox.insertItem(0,toolbar,'BTN')



app = QApplication(sys.argv)

screen = window()
screen.show()


app2 = QApplication(sys.argv)

screen2 = window2()
screen2.show()

sys.exit(app.exec_() and app2.exec_())