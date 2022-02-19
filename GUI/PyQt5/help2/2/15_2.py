from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global combobox,button
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        combobox=QComboBox()
        combobox.addItem("python")
        combobox.addItem("c++")
        combobox.addItem("java")
        layout.addWidget(combobox)
        combobox.currentTextChanged.connect(self.comboboxchanged)
        button=QPushButton("show popup")
        layout.addWidget(button)
        button.clicked.connect(self.buttonclicked)
        button.hide()
        combobox.setEditable(True)
        combobox.setMaxVisibleItems(2)
    def comboboxchanged(self):
        text=combobox.currentText()
        print(text)
        if text=="java":
            button.show()
        else:
            button.hide()
    def buttonclicked(self):
        combobox.showPopup()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
