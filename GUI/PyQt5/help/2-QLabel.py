from PyQt5.QtWidgets import *
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        label = QLabel('MyLabel')
        layout.addWidget(label)
        label.setIndent(10)
        label.setMargin(50)

app = QApplication(sys.argv)
screen = window()
screen.show()

sys.exit(app.exec_())