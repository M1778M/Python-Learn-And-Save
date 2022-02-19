from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        options=["c++","python","java","php"]
        completer=QCompleter(options)
        lineedit=QLineEdit()
        lineedit.setCompleter(completer)
        layout.addWidget(lineedit)
        completer.setMaxVisibleItems(1)
        completer.setCompletionMode(QCompleter.InlineCompletion)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
