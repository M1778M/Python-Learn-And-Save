from PyQt5.QtWidgets import *
import sys
class window(QWidget):
    def __init__(self):
        global filedialog,colordialog,label,button,button2,button3
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        self.resize(600,600)
        dialog=QDialogButtonBox(QDialogButtonBox.Close | QDialogButtonBox.Ok)
        layout.addChildWidget(dialog)
        dialog.setGeometry(300,200,200,100)
        filedialog=QFileDialog()
        button=QPushButton("filedialog")
        layout.addWidget(button)
        button.clicked.connect(self.on_click)
        button2=QPushButton("Filename")
        layout.addWidget(button2)
        button2.clicked.connect(self.on_click2)
        filedialog.setAcceptMode(QFileDialog.AcceptOpen)
        colordialog=QColorDialog()
        button3=QPushButton("color")
        layout.addWidget(button3)
        button3.clicked.connect(self.on_click3)
        label=QLabel("label")
        layout.addWidget(label)
    def on_click(self):
        global fname
        fname=filedialog.getOpenFileName()
    def on_click2(self):
        print(fname)
        label.setText(fname[0])
    def on_click3(self):
        color=QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            button.setStyleSheet("background-color:"+color.name()+";")
            button2.setStyleSheet("background-color:"+color.name()+";")
            button3.setStyleSheet("background-color:"+color.name()+";")
app=QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())
