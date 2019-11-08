# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrew Wiraatmaja\Documents\Mini Project CZ1003\Stall_Info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Check_Queue import Ui_CheckQueue

import pickle
from Database import Stall
from Database import item

from datetime import date
import calendar

d = date.today()
year = d.year
month = d.month
day = d.day

dayy = (calendar.weekday(year,month,day)+2)%7

data_file = open("stall_info.out", mode="rb")
db = pickle.load(data_file)
data_file.close()

list_stall = []
list_pic = ["McDonald.png","italian.png","pizzahut.png"]
index = 0

for i in range(3):
    list_stall.append(db[i].st_name)

class Ui_StallInfo(object):

    def displayStall(self):
        MainWindow.resize(800, 630)
        self.ch_stall.hide()
        self.comboBox.hide()
        self.proceed.hide()
        text = str(self.comboBox.currentText())
        self.stall_name.setText(text)
        for i in range(3) :
            if db[i].st_name == text :
                index = i
        self.stall_name.show()
        self.logo.setPixmap(QtGui.QPixmap(list_pic[index]))
        self.logo.setScaledContents(True)
        self.logo.show()
        self.desc.setText(db[index].desc)
        self.desc.show()
        self.open_time.setText(db[index].opening_time[dayy])
        self.open_time.show()
        self.close_time.setText(db[index].closing_time[dayy])
        self.close_time.show()
        self.prep_time.setText(str(float(db[index].prep_time)))
        self.prep_time.show()
        self.change_time.setText(db[index].changeover_time[dayy])
        self.change_time.show()
        if db[index].halal == True :
            self.halal.setPixmap(QtGui.QPixmap("halal.webp"))
            self.halal.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.pushButton.show()
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckQueue()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ch_stall = QtWidgets.QLabel(self.centralwidget)
        self.ch_stall.setGeometry(QtCore.QRect(30, 30, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(20)

        self.ch_stall.setFont(font)
        self.ch_stall.setAutoFillBackground(True)
        self.ch_stall.setAlignment(QtCore.Qt.AlignCenter)
        self.ch_stall.setObjectName("ch_stall")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 311, 61))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        for i in range(3):
            self.comboBox.addItem(QtGui.QIcon(list_pic[i]),list_stall[i],font)

        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(180, 220, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proceed.setFont(font)
        self.proceed.setObjectName("proceed")
        self.proceed.clicked.connect(self.displayStall)

        self.stall_name = QtWidgets.QLabel(self.centralwidget)
        self.stall_name.setGeometry(QtCore.QRect(240, 30, 311, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.stall_name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(20)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.stall_name.setFont(font)
        self.stall_name.setAlignment(QtCore.Qt.AlignCenter)
        self.stall_name.setObjectName("stall_name")
        self.stall_name.hide()

        self.desc = QtWidgets.QLabel(self.centralwidget)
        self.desc.setGeometry(QtCore.QRect(110, 120, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc.setFont(font)
        self.desc.setAlignment(QtCore.Qt.AlignCenter)
        self.desc.setObjectName("desc")
        self.desc.hide()

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(120, 30, 141, 81))
        self.logo.setObjectName("logo")
        self.logo.hide()

        self.halal = QtWidgets.QLabel(self.centralwidget)
        self.halal.setGeometry(QtCore.QRect(580, 40, 51, 61))
        self.halal.setObjectName("halal")
        self.halal.hide()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 180, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 220, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()

        self.open_time = QtWidgets.QLabel(self.centralwidget)
        self.open_time.setGeometry(QtCore.QRect(210, 180, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.open_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.open_time.setFont(font)
        self.open_time.setObjectName("open_time")
        self.open_time.hide()

        self.close_time = QtWidgets.QLabel(self.centralwidget)
        self.close_time.setGeometry(QtCore.QRect(210, 220, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.close_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.close_time.setFont(font)
        self.close_time.setObjectName("close_time")
        self.close_time.hide()

        self.prep_time = QtWidgets.QLabel(self.centralwidget)
        self.prep_time.setGeometry(QtCore.QRect(600, 180, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.prep_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.prep_time.setFont(font)
        self.prep_time.setObjectName("prep_time")
        self.prep_time.hide()

        self.change_time = QtWidgets.QLabel(self.centralwidget)
        self.change_time.setGeometry(QtCore.QRect(600, 220, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.change_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(12)
        self.change_time.setFont(font)
        self.change_time.setObjectName("change_time")
        self.change_time.hide()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 280, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(27)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 500, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.hide()
        self.pushButton.clicked.connect(self.openWindow)

        self.name_menu1 = QtWidgets.QLabel(self.centralwidget)
        self.name_menu1.setGeometry(QtCore.QRect(50, 350, 311, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.name_menu1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(18)
        self.name_menu1.setFont(font)
        self.name_menu1.setObjectName("name_menu1")
        self.name_menu1.hide()

        self.name_menu2 = QtWidgets.QLabel(self.centralwidget)
        self.name_menu2.setGeometry(QtCore.QRect(50, 420, 311, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.name_menu2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(18)
        self.name_menu2.setFont(font)
        self.name_menu2.setObjectName("name_menu2")
        self.name_menu2.hide()

        self.price_menu1 = QtWidgets.QLabel(self.centralwidget)
        self.price_menu1.setGeometry(QtCore.QRect(600, 360, 151, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.price_menu1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(18)
        self.price_menu1.setFont(font)
        self.price_menu1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_menu1.setObjectName("price_menu1")
        self.price_menu1.hide()

        self.price_menu2 = QtWidgets.QLabel(self.centralwidget)
        self.price_menu2.setGeometry(QtCore.QRect(600, 420, 151, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.price_menu2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(18)
        self.price_menu2.setFont(font)
        self.price_menu2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_menu2.setObjectName("price_menu2")
        self.price_menu2.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ch_stall.setText(_translate("MainWindow", "Choose Stall"))
        self.label_2.setText(_translate("MainWindow", "Opening Hours :"))
        self.label_3.setText(_translate("MainWindow", "Closing Hours :"))
        self.label_4.setText(_translate("MainWindow", "Preparation Time :"))
        self.label_5.setText(_translate("MainWindow", "Changeover Time :"))
        self.label_6.setText(_translate("MainWindow", "Menu"))
        self.pushButton.setText(_translate("MainWindow", "Check Queue"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StallInfo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())