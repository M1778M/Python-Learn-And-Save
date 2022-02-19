from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        mb=QMessageBox()
        layout.addWidget(mb)
        mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Reset)
        mb.setText("WARNING! ")
        mb.setInformativeText("This Application can not be installed on Windows.")
        mb.setIcon(QMessageBox.Critical)
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
