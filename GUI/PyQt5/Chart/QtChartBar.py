from PyQt5.QtChart import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        
        set = QBarSet('Persion')
        
        set << 10 << 20 << 30 << 40 << 50 << 60 << 70 << 80 << 90 << 100
        
        series = QPercentBarSeries() 
        
        series.append(set)
        
        chart = QChart()
        
        chart.addSeries(series)
        
        chart.setTitle('Test')
        
        chart.setTheme(QChart.ChartThemeDark)
        
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        catg = ['Testable']
        
        axis = QBarCategoryAxis()
        axis.append(catg)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        
        chartview = QChartView(chart)
        
        layout.addWidget(chartview)
        
        self.show()


app = QApplication(sys.argv)
sc = window()
sys.exit(app.exec_())
