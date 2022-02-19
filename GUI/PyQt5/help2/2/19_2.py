from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global fontcombobox
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        fontcombobox=QFontComboBox()
        layout.addWidget(fontcombobox)
        fontcombobox.currentFontChanged.connect(self.fontchanged)
    def fontchanged(self):
        font=fontcombobox.currentFont()
        print("font:  %s " % (font.family()))
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
