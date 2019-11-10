# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrew Wiraatmaja\Documents\Mini Project CZ1003\Stall_Info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import pickle
from Database import Stall
from Database import item

from datetime import date
import calendar

list_pic = ["Subway_logo_brand.png","pizzahut.png","malay_food.jpg","McDonald.png",  "chicken_rice.jpg", ""]

class Ui_StallInfo(object):
    
    def displayStall(self):
        d = date.today()
        year = d.year
        month = d.month
        day = d.day

        dayy = (calendar.weekday(year,month,day)+2)%7

        data_file = open("stall_info.out", mode="rb")
        db = pickle.load(data_file)
        data_file.close()

         
        
        index = 0

        
        self.ch_stall.hide()
        self.comboBox.hide()
        self.proceed.hide()
        text = str(self.comboBox.currentText())
        self.stall_name.setText(text)
        for i in range(len(db)) :
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
        self.back.show()
        self.pushButton.hide()
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckQueue()
        self.ui.setupUi(self.window)
        self.window.show()

    def backButton(self):
        self.ch_stall.show()
        self.comboBox.show()
        self.proceed.show()
        self.stall_name.hide()
        self.logo.hide()
        self.desc.hide()
        self.open_time.hide()
        self.close_time.hide()
        self.prep_time.hide()
        self.change_time.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.back.hide()
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 161, 51))


    def setupUi(self, FirstWindow):
        data_file = open("stall_info.out", mode="rb")
        db = pickle.load(data_file)
        data_file.close()

         
        

        
        
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.ch_stall = QtWidgets.QLabel(self.centralwidget)
        self.ch_stall.setGeometry(QtCore.QRect(130, 130, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(25)
        self.ch_stall.setFont(font)
        self.ch_stall.setAutoFillBackground(True)
        self.ch_stall.setAlignment(QtCore.Qt.AlignCenter)
        self.ch_stall.setObjectName("ch_stall")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 240, 311, 61))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        for i in range(len(db)):
            self.comboBox.addItem(QtGui.QIcon(list_pic[i]),db[i].st_name,font)

        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(300, 330, 161, 51))
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
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton.hide()

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

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 40, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.back.hide()
        self.back.clicked.connect(self.backButton)

        FirstWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FirstWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        FirstWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setObjectName("statusbar")
        FirstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "FirstWindow"))
        self.ch_stall.setText(_translate("FirstWindow", "Choose Stall"))
        self.label_2.setText(_translate("FirstWindow", "Opening Hours :"))
        self.label_3.setText(_translate("FirstWindow", "Closing Hours :"))
        self.label_4.setText(_translate("FirstWindow", "Preparation Time :"))
        self.label_5.setText(_translate("FirstWindow", "Changeover Time :"))
        self.label_6.setText(_translate("FirstWindow", "Menu"))
        self.pushButton.setText(_translate("FirstWindow", "Check Queue"))
        self.proceed.setText(_translate("FirstWindow", "Menu"))
        self.back.setText(_translate("FirstWindow","Back"))

class Ui_CheckQueue(object):

    def calcQueue(self):
        self.pushButton.hide()
        self.label_5.show()
        self.label_6.show()
        self.label_7.show()
        self.textEdit.hide()
        num = self.textEdit.toPlainText()
        tim = float(float(num) * 2)
        self.label_6.setText(str(int(tim))+" mins")
        self.label_7.setText(str(int(num))+" ppl")
        self.back.show() 
    
    def backButton(self):
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.pushButton.show()
        self.textEdit.show()
        self.back.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 581, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 371, 41))
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
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 130, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calcQueue)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 40, 371, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 381, 41))
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
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.hide()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 220, 121, 41))
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
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 130, 81, 71))
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
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_5")
        self.label_7.hide()

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 40, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.back.hide()
        self.back.clicked.connect(self.backButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 31))
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
        self.label_3.setText(_translate("MainWindow", "Number of People Queueing"))
        self.pushButton.setText(_translate("MainWindow", "Check Queue"))
        self.label_4.setText(_translate("MainWindow", "Check Queue"))
        self.label_5.setText(_translate("MainWindow", "Time needed for Queueing is"))
        self.label_6.setText(_translate("MainWindow", "mins"))
        self.back.setText(_translate("MainWindow","Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_StallInfo()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())
