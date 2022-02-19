from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global wizard
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        button=QPushButton("Launch")
        button.clicked.connect(self.click)
        layout.addWidget(button)
        button2=QPushButton("Back")
        button2.clicked.connect(self.click2)
        layout.addWidget(button2)
        wizard=QWizard()
        w=QWizardPage()
        w2=QWizardPage()
        wizard.setPage(1,w)
        w.setTitle("This is page 1")
        w.setSubTitle("Faradars")
        wizard.setPage(2,w2)
        w2.setTitle("This is page 2")
    def click(self):
        wizard.open()
    def click2(self):
        wizard.restart()
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
