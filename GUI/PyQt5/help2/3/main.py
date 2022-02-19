from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pandas as pd
from fpdf import FPDF
import winsound

me=["comb1"]

maincss=("""QScrollArea{
           border-radius: 10px;
           max-width: 1980px;
           min-width: 850px;
           max-height: 450px;
           min-height: 450px;
           background-color: rgb(255, 255, 255);
           color: rgb(255, 255, 255);}""")
maincss2=("""QScrollArea{
           border-radius: 10px;
           max-width: 1980px;
           min-width: 850px;
           max-height: 80px;
           min-height: 70px;}""")
maincss3=("""QScrollArea{
           border-radius: 10px;
           max-width: 1980px;
           min-width: 850px;
           max-height: 120px;
           min-height: 110px;}""")
tablecss=("""QTableWidget{
           border-radius: 5px;
           max-width: 1900px;
           min-width: 350px;
           max-height: 400px;
           min-height: 400px;
           border:2px solid  rgb(0,0,0);
           font-size: 16px;
           background-color: rgb(255, 255, 255);
           margin-left: 10px;}""")
buttoncss=("""QPushButton{
           background-color: rgb(50,250,50);
           border-radius: 10px;
           max-width: 1950px;
           min-width: 150px;
           max-height: 30px;
           min-height: 30px;
           border:2px solid  rgb(0,0,0);
           font-size: 12px;}"""+
           """QPushButton:hover{
           background-color: rgb(250,250,50);
        }""")

linecss=("""QLineEdit{
           border-radius: 8px;
           max-width: 445px;
           min-width: 240px;
           max-height: 25px;
           min-height: 25px;
           border:2px solid  rgb(235, 213, 170);
           background-color: rgb(255, 252, 200);
           font-size: 18px;
           color: rgb(0, 0, 0);}
           """+
           """QLineEdit:focus{
          border:2px solid  rgb(108, 172, 205);
        }""")
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        self.resize(1100,600)

        self.firstsublayout=QScrollArea()
        self.firstsublayout.setAlignment(Qt.AlignCenter)
        self.firstsublayout.setWidgetResizable(True)
        self.layout.addWidget(self.firstsublayout)
        self.widget = QWidget()
        self.firstsublayout.setWidget(self.widget)
        self.firstsublayoutadd = QGridLayout(self.widget)
        self.firstsublayoutadd.setAlignment(Qt.AlignJustify)
        self.firstsublayout.setStyleSheet(maincss)

        self.tw=QTableWidget()
        self.firstsublayoutadd.addWidget(self.tw)
        self.tw.setRowCount(0)
        self.tw.setColumnCount(4)
        headerv = self.tw.horizontalHeader()
        self.tw.resizeColumnsToContents()
        headerv.setSectionResizeMode(QHeaderView.Stretch)
        xlsxcolumns=["Name","P-Number","Unit","Price($)"]
        self.tw.setHorizontalHeaderLabels(xlsxcolumns)
        self.tw.setStyleSheet(tablecss)
        self.tw.itemChanged.connect(self.twchanged)

        self.secondsublayout=QScrollArea()
        self.secondsublayout.setAlignment(Qt.AlignCenter)
        self.secondsublayout.setWidgetResizable(True)
        self.layout.addWidget(self.secondsublayout)
        self.widget = QWidget()
        self.secondsublayout.setWidget(self.widget)
        self.secondsublayoutadd2 = QGridLayout(self.widget)
        self.secondsublayoutadd2.setAlignment(Qt.AlignJustify)
        self.secondsublayout.setStyleSheet(maincss2)

        self.addproduct=QPushButton("Add Product")
        self.secondsublayoutadd2.addWidget(self.addproduct,0,0)
        self.addproduct.clicked.connect(self.addp)
        self.addproduct.setStyleSheet(buttoncss)

        self.deleteproduct=QPushButton("Delete Product")
        self.secondsublayoutadd2.addWidget(self.deleteproduct,0,1)
        self.deleteproduct.clicked.connect(self.delp)
        self.deleteproduct.setStyleSheet(buttoncss)

        self.clearproduct=QPushButton("Clear All")
        self.secondsublayoutadd2.addWidget(self.clearproduct,0,2)
        self.clearproduct.clicked.connect(self.clearp)
        self.clearproduct.setStyleSheet(buttoncss)

        self.df = pd.read_excel (r'list.xlsx',dtype=str)
        self.firstc = self.df['name'].values.tolist()


        self.thirdsublayout=QScrollArea()
        self.thirdsublayout.setAlignment(Qt.AlignCenter)
        self.thirdsublayout.setWidgetResizable(True)
        self.layout.addWidget(self.thirdsublayout)
        self.widget = QWidget()
        self.thirdsublayout.setWidget(self.widget)
        self.thirdsublayoutadd3 = QGridLayout(self.widget)
        self.thirdsublayoutadd3.setAlignment(Qt.AlignJustify)
        self.thirdsublayout.setStyleSheet(maincss3)

        self.subpricet=QLabel("Subprice($):")
        self.thirdsublayoutadd3.addWidget(self.subpricet,0,0)
        self.subprice=QLineEdit()
        self.thirdsublayoutadd3.addWidget(self.subprice,1,0)
        self.subprice.setReadOnly(True)
        self.subprice.setStyleSheet(linecss)

        self.taxvalue=0
        self.taxt=QLabel("Tax($):")
        self.thirdsublayoutadd3.addWidget(self.taxt,0,1)
        self.tax=QLineEdit()
        self.tax.setText(str(self.taxvalue))
        self.tax.textChanged.connect(self.linechanged)
        self.thirdsublayoutadd3.addWidget(self.tax,1,1)
        self.tax.setStyleSheet(linecss)

        self.discountvalue=0
        self.discountt=QLabel("Discount(%):")
        self.thirdsublayoutadd3.addWidget(self.discountt,0,2)
        self.discount=QLineEdit()
        self.discount.setText(str(self.discountvalue))
        self.discount.textChanged.connect(self.linechanged)
        self.thirdsublayoutadd3.addWidget(self.discount,1,2)
        self.discount.setStyleSheet(linecss)

        self.totalt=QLabel("Total($):")
        self.thirdsublayoutadd3.addWidget(self.totalt,0,3)
        self.total=QLineEdit()
        self.thirdsublayoutadd3.addWidget(self.total,1,3)
        self.total.setReadOnly(True)
        self.total.setStyleSheet(linecss)

        self.pdfbutton=QPushButton("Print PDF")
        self.thirdsublayoutadd3.addWidget(self.pdfbutton,2,3)
        self.pdfbutton.setStyleSheet(buttoncss)
        self.pdfbutton.clicked.connect(self.printit)

    def updateproduct(self):
        self.df = pd.read_excel (r'list.xlsx',dtype=str)
        self.firstc = self.df['name'].values.tolist()
        rowcountupdate=self.tw.rowCount()
        me.append("comb"+str(rowcountupdate))
        me[-1]=QComboBox()
        me[-1].addItems(self.firstc)
        self.tw.setCellWidget(rowcountupdate-1,0,me[-1])
        me[-1].currentIndexChanged.connect(self.combochange)

    def addp(self):
        addnewrow=self.tw.rowCount()+1
        self.tw.setRowCount(addnewrow)
        self.updateproduct()

    def delp(self):
        delrow=self.tw.rowCount()-1
        self.tw.setRowCount(delrow)
        self.tw.setColumnCount(4)
        try:
            del me[-1]
        except:
            pass
        self.combochange(None)


    def clearp(self):
        me.clear()
        mysubprice=0
        self.tw.setRowCount(0)
        self.tw.setColumnCount(4)
        self.subprice.setText("0")
        self.total.setText("0")
        xlsxcolumns=["Name","P-Number","Unit","Price($)"]
        self.tw.setHorizontalHeaderLabels(xlsxcolumns)
        self.updateproduct()

    def combochange(self,count):
        mysubprice=0
        try:
            sending_cell = self.sender()
            selectedrow=me.index(sending_cell)
            for col in range(3):
                self.tw.setItem(selectedrow-1, col+1,QTableWidgetItem(str(self.df.iloc[count][col+1])))
        except:
            pass
        for rows in range (self.tw.rowCount()):
            try:
                hazine=self.tw.item(rows, 3)
                unit=self.tw.item(rows, 2)
                mysubprice+=(float(hazine.text())*int(unit.text()))
            except:
                pass

        try:
            self.subprice.setText(str(mysubprice))
            totalprice=(mysubprice+float(self.tax.text()))*((100-int(self.discount.text()))/100)
            self.total.setText(str(totalprice))
        except:
            pass

    def twchanged(self):
        self.combochange(None)

    def linechanged(self):
        self.combochange(None)
########################################################################
    def printit(self):
        spacing=1
        data1 = ["Name","P-Number","Unit","Price($)"]
        data2=[]
        print(self.tw.rowCount())
        for rows in range(self.tw.rowCount()):
            data2.append([])
            print(data2)
            for cols in range (self.tw.columnCount()):
                try:
                    data2_item=self.tw.item(rows,cols)
                    data2[rows].append(data2_item.text())
                except:
                    try:
                        data2_item=self.tw.cellWidget(rows,cols)
                        data2[rows].append(data2_item.currentText())
                    except:
                        pass
        print(data2)
        pdf = FPDF()

        pdf.add_font('BRLNSDB','', 'BRLNSDB.TTF', uni=True)
        pdf.set_font("BRLNSDB", size=30)
        pdf.set_text_color(0, 0, 0)
        pdf.set_fill_color(255, 255, 255)
        pdf.add_page()
        pdf.cell(200, 30, txt = "Company Name",ln = 2, align = 'C')

        # add another cell
        col_width = pdf.w / 4.5
        row_height = pdf.font_size
        pdf.add_font('calibrib','', 'calibrib.ttf', uni=True)
        pdf.set_font("calibrib", size=12)
        pdf.cell(30, 5, txt = "",ln = 2, align = 'L')
        pdf.image('logo.png',138,32,60,50,'PNG','www.faradars.org');
        pdf.cell(30, 10, txt = "Name:",ln = 2, align = 'L')
        pdf.cell(30, 10, txt = "Date:",ln = 2, align = 'L')
        pdf.cell(30, 10, txt = "Address: Faradars",ln = 2, align = 'L')
        pdf.cell(30, 5, txt = "",ln = 2, align = 'L')
        for item in data1:
            pdf.set_fill_color(200, 200, 200)
            pdf.cell(col_width, row_height*spacing*1.2,txt=item,border=1,align="C",fill=1)
        pdf.ln(row_height*spacing*1.2)
        for row in data2:
            for item in row:
                pdf.set_fill_color(245, 245, 245)
                pdf.cell(col_width, row_height*spacing,txt=item,border=1,align="C",fill=1)
            pdf.ln(row_height*spacing)
        pdf.cell(30, 15, txt = "",ln = 2, align = 'L')
        data3=[['Subprice:', str("{:.2f}".format(float(self.subprice.text())))+" $"],
                ['Tax:', str(self.tax.text())+" $"],
                ['Discount:', str(self.discount.text())+" %"],
                ['Total Price:',str("{:.2f}".format(float(self.total.text())))+" $"]]
        for row in data3:
            for item in row:
                pdf.set_fill_color(225, 225, 225)
                pdf.cell(col_width, row_height*spacing,txt=item,border=1,align="C",fill=1)
            pdf.ln(row_height*spacing)
        pdf.output('out.pdf')
        winsound.Beep(940, 550) # frequency, duration

#########################################################################################################

app=QApplication(sys.argv)
screen=window()
screen.showFullScreen()
sys.exit(app.exec_())
