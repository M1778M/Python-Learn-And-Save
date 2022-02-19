from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global label,lineedit,lineedit2
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,500)
        lineedit=QLineEdit()
        layout.addWidget(lineedit,0,0)
        lineedit.setPlaceholderText("Name")
        lineedit.returnPressed.connect(self.press)
        lineedit2=QLineEdit()
        layout.addWidget(lineedit2,1,0)
        lineedit2.setPlaceholderText("Family Name")
        lineedit2.returnPressed.connect(self.press)
        label=QLabel("label")
        layout.addWidget(label)
        lineedit.setMaxLength(6)
        lineedit2.setMaxLength(8)
    def press(self):
        label.setText("Fullname of user is: "+lineedit.text()+" "+lineedit2.text())
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
