from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global dspinbox
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        dspinbox=QDoubleSpinBox()
        layout.addWidget(dspinbox)
        dspinbox.setRange(0,1)
        dspinbox.setPrefix("Value  ")
        dspinbox.setSuffix("  cm")
        dspinbox.setSingleStep(0.01)
        dspinbox.valueChanged.connect(self.dspinchanged)
    def dspinchanged(self):
        print(dspinbox.value())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
