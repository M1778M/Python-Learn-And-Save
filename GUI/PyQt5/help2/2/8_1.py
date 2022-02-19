from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global spinbox
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        spinbox=QSpinBox()
        layout.addWidget(spinbox)
        spinbox.setRange(0,100)
        spinbox.setPrefix("value  ")
        spinbox.setSuffix("  cm")
        spinbox.setSingleStep(2)
        spinbox.valueChanged.connect(self.spinchange)
    def spinchange(self):
        print(spinbox.value())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
