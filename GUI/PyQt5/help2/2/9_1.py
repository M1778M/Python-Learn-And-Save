from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global dial,label
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        dial=QDial()
        layout.addWidget(dial)
        dial.setMinimum(0)
        dial.setMaximum(100)
        dial.setValue(0)
        dial.valueChanged.connect(self.dialchange)
        label=QLabel("label")
        layout.addWidget(label)
    def dialchange(self):
        print(dial.value())
        if dial.value()==0:
            label.setText("minimum")
        elif dial.value()==100:
            label.setText("maximum")
        else:
            label.setText("mid")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
