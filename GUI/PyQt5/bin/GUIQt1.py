# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIQt1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 433)
        MainWindow.setStyleSheet("background-color:#232a35;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.username.setStyleSheet("background-color:#fff;border:1px solid rgb(136,173,236) ;")
        self.username.setObjectName("username")
        self.passowrd = QtWidgets.QLineEdit(self.centralwidget)
        self.passowrd.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.passowrd.setStyleSheet("background-color:#fff;border:1px solid rgb(136,173,236) ;")
        self.passowrd.setInputMask("")
        self.passowrd.setMaxLength(30)
        self.passowrd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passowrd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.passowrd.setObjectName("passowrd")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(40, 150, 75, 23))
        self.button.setStyleSheet("background-color:#fff;border:1.4px  solid #000 ;color:#024;border-radius:1%;")
        self.button.setObjectName("button")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(220, 0, 281, 331))
        self.table.setStyleSheet("border:1px solid;background-color:;color:rgb(29,74,15);\n"
"padding:4px;\n"
"")
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.outputdown = QtWidgets.QTextEdit(self.centralwidget)
        self.outputdown.setGeometry(QtCore.QRect(0, 330, 501, 61))
        self.outputdown.setStyleSheet("border:1.5px solid #000;color:#000;padding:4px;")
        self.outputdown.setObjectName("outputdown")
        self.onprocess = QtWidgets.QProgressBar(self.centralwidget)
        self.onprocess.setGeometry(QtCore.QRect(20, 300, 191, 23))
        self.onprocess.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.onprocess.setStyleSheet("color:white;")
        self.onprocess.setProperty("value", 0)
        self.onprocess.setObjectName("onprocess")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button.clicked.connect(MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI-Project"))
        self.button.setText(_translate("MainWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
