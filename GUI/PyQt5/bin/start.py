#!
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

window = QWidget()

window.setGeometry(100,100,1000,600)

window.setWindowTitle("StartProfuckingGrammming")

window.setWindowIcon(QIcon('C:\\Users\\m1778\\M1778\\XIco.ico'))

window.show()


sys.exit(app.exec_())
