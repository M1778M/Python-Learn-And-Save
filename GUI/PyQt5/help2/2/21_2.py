from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global label,textedit
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,500)
        textedit=QTextEdit()
        textedit.setPlaceholderText("Describe yourself: ")
        textedit.textChanged.connect(self.press)
        layout.addWidget(textedit,0,0)
        label=QLabel("press enter to show the text.")
        layout.addWidget(label)
        button=QPushButton("undo")
        layout.addWidget(button)
        button.clicked.connect(self.clickundo)
        button2=QPushButton("redo")
        layout.addWidget(button2)
        button2.clicked.connect(self.clickredo)
    def press(self):
        label.setText(textedit.toPlainText())
    def clickundo(self):
        textedit.undo()
    def clickredo(self):
        textedit.redo()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
