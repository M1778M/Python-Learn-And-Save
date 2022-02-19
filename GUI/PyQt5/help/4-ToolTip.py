#----------ToolTip--------
# widget.setToolTip(str(text))
# { for Get More Infomation from WhatsThis press [Shift+F1]}
#----------WhatsThis------
# widget.setWhatsThis(str(text))
from PyQt5.QtWidgets import *
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(500,500)
        btn = QPushButton('btn1')
        btn2 = QPushButton('btn2')
        btn3 = QPushButton('btn3')
        btn.setToolTip('Tooltip btn1')
        btn2.setToolTip('ToolTip btn2')
        btn3.setWhatsThis('whatsthis btn3')
        layout.addWidget(btn,0,0)
        layout.addWidget(btn2,1,0)
        layout.addWidget(btn3,2,0)

app = QApplication(sys.argv)
screen=window()
screen.show()
sys.exit(app.exec_())