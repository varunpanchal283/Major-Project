# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
import pickle
import threading
import configparser
import css
import sys

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(722, 565)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(280, 10, 421, 541))
		self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.widget.setObjectName("widget")
		self.pickle_b = QtWidgets.QPushButton(self.widget)
		self.pickle_b.setGeometry(QtCore.QRect(50, 30, 81, 31))
		self.pickle_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.971591, y2:0.006, stop:0 rgba(0, 245, 255, 255), stop:1 rgba(125, 243, 218, 255));\n"
"border-radius: 15px;\n"
"font: 75 12pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.pickle_b.setObjectName("pickle_b")
		self.config_b = QtWidgets.QPushButton(self.widget)
		self.config_b.setGeometry(QtCore.QRect(300, 30, 81, 31))
		self.config_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.971591, y2:0.006, stop:0 rgba(0, 245, 255, 255), stop:1 rgba(125, 243, 218, 255));\n"
"border-radius: 15px;\n"
"font: 75 12pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.config_b.setObjectName("config_b")
		self.brand_c = QtWidgets.QComboBox(self.widget)
		self.brand_c.setGeometry(QtCore.QRect(220, 90, 171, 21))
		self.brand_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.brand_c.setObjectName("brand_c")
		self.model_c = QtWidgets.QComboBox(self.widget)
		self.model_c.setGeometry(QtCore.QRect(220, 140, 171, 21))
		self.model_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.model_c.setObjectName("model_c")
		self.place_c = QtWidgets.QComboBox(self.widget)
		self.place_c.setGeometry(QtCore.QRect(220, 190, 171, 21))
		self.place_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.place_c.setObjectName("place_c")
		self.fuel_c = QtWidgets.QComboBox(self.widget)
		self.fuel_c.setGeometry(QtCore.QRect(220, 240, 171, 21))
		self.fuel_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.fuel_c.setObjectName("fuel_c")
		self.year_c = QtWidgets.QComboBox(self.widget)
		self.year_c.setGeometry(QtCore.QRect(220, 290, 171, 21))
		self.year_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.year_c.setObjectName("year_c")
		self.owner_c = QtWidgets.QComboBox(self.widget)
		self.owner_c.setGeometry(QtCore.QRect(220, 390, 171, 21))
		self.owner_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.owner_c.setObjectName("owner_c")
		self.engine_c = QtWidgets.QComboBox(self.widget)
		self.engine_c.setGeometry(QtCore.QRect(220, 440, 171, 21))
		self.engine_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.engine_c.setObjectName("engine_c")
		self.label = QtWidgets.QLabel(self.widget)
		self.label.setGeometry(QtCore.QRect(50, 80, 81, 41))
		self.label.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.widget)
		self.label_2.setGeometry(QtCore.QRect(50, 130, 81, 41))
		self.label_2.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.widget)
		self.label_3.setGeometry(QtCore.QRect(50, 180, 81, 41))
		self.label_3.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.widget)
		self.label_4.setGeometry(QtCore.QRect(50, 230, 101, 41))
		self.label_4.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.widget)
		self.label_5.setGeometry(QtCore.QRect(50, 280, 151, 41))
		self.label_5.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.widget)
		self.label_6.setGeometry(QtCore.QRect(50, 330, 141, 41))
		self.label_6.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.widget)
		self.label_7.setGeometry(QtCore.QRect(50, 380, 121, 41))
		self.label_7.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.widget)
		self.label_8.setGeometry(QtCore.QRect(50, 430, 151, 41))
		self.label_8.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.label_8.setObjectName("label_8")
		self.getprice_b = QtWidgets.QPushButton(self.widget)
		self.getprice_b.setGeometry(QtCore.QRect(50, 490, 81, 31))
		self.getprice_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.971591, y2:0.006, stop:0 rgba(0, 245, 255, 255), stop:1 rgba(125, 243, 218, 255));\n"
"border-radius: 15px;\n"
"font: 75 12pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.getprice_b.setObjectName("getprice_b")
		self.result = QtWidgets.QLabel(self.widget)
		self.result.setGeometry(QtCore.QRect(150, 495, 251, 21))
		self.result.setStyleSheet("font: 75 19pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.result.setText("")
		self.result.setObjectName("result")
		self.milage_c = QtWidgets.QLineEdit(self.widget)
		self.milage_c.setGeometry(QtCore.QRect(220, 340, 171, 20))
		self.milage_c.setStyleSheet("font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;")
		self.milage_c.setText("")
		self.milage_c.setObjectName("milage_c")
		self.widget_2 = QtWidgets.QWidget(self.centralwidget)
		self.widget_2.setGeometry(QtCore.QRect(20, 10, 291, 541))
		self.widget_2.setStyleSheet("background-color: rgb(62, 210, 255);\n"
"border-radius: 25px;")
		self.widget_2.setObjectName("widget_2")
		self.widget_3 = QtWidgets.QWidget(self.widget_2)
		self.widget_3.setGeometry(QtCore.QRect(40, 20, 221, 91))
		self.widget_3.setStyleSheet("image: url(:/newPrefix/Car2 copy.png);")
		self.widget_3.setObjectName("widget_3")
		self.label_9 = QtWidgets.QLabel(self.widget_2)
		self.label_9.setGeometry(QtCore.QRect(40, 110, 231, 21))
		self.label_9.setStyleSheet("font: 75 17pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.label_9.setObjectName("label_9")
		self.connect = QtWidgets.QPushButton(self.widget_2)
		self.connect.setGeometry(QtCore.QRect(120, 170, 51, 51))
		self.connect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"border-radius: 20px;\n"
"")
		self.connect.setObjectName("connect")
		self.exit_b = QtWidgets.QPushButton(self.widget_2)
		self.exit_b.setGeometry(QtCore.QRect(120, 420, 51, 51))
		self.exit_b.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"border-radius: 20px;\n"
"")
		self.exit_b.setObjectName("exit_b")
		self.label_10 = QtWidgets.QLabel(self.widget_2)
		self.label_10.setGeometry(QtCore.QRect(40, 260, 221, 21))
		self.label_10.setStyleSheet("font: 75 13pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(self.widget_2)
		self.label_11.setGeometry(QtCore.QRect(40, 290, 231, 21))
		self.label_11.setStyleSheet("font: 75 13pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(self.widget_2)
		self.label_12.setGeometry(QtCore.QRect(40, 320, 231, 21))
		self.label_12.setStyleSheet("font: 75 13pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"color: rgb(255, 255, 255);")
		self.label_12.setObjectName("label_12")
		MainWindow.setCentralWidget(self.centralwidget)
		self.pickle_b.clicked.connect(self.choose_pickle)
		self.config_b.clicked.connect(self.choose_config)
		self.getprice_b.clicked.connect(self.getprice)
		self.connect.clicked.connect(self.open_url)
		self.exit_b.clicked.connect(self.exit_f)
		self.connect.setStyleSheet('''
			QPushButton
			{
			background-color: rgb(255, 255, 255);
			font: 75 9pt "Agency FB";
			font-weight: Bold;
			border-radius: 25px;
			}
			QPushButton::hover
			{
			color: rgb(0, 5, 255);
			font: 75 12pt "Agency FB";
			font-weight: Bold;
			background-color: rgb(255, 230, 212);
			}
			''')
		self.exit_b.setStyleSheet('''
			QPushButton
			{
			background-color: rgb(255, 255, 255);
			font: 75 9pt "Agency FB";
			font-weight: Bold;
			border-radius: 25px;
			}
			QPushButton::hover
			{
			color: rgb(255,0,0);
			font: 75 10pt "Agency FB";
			font-weight: Bold;
			}
			''')

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pickle_b.setText(_translate("MainWindow", "MODEL"))
		self.config_b.setText(_translate("MainWindow", "CONFIG"))
		self.label.setText(_translate("MainWindow", "Brand"))
		self.label_2.setText(_translate("MainWindow", "Model"))
		self.label_3.setText(_translate("MainWindow", "Place"))
		self.label_4.setText(_translate("MainWindow", "Engine Type"))
		self.label_5.setText(_translate("MainWindow", "Manufactured Year"))
		self.label_6.setText(_translate("MainWindow", "Odometer Reading"))
		self.label_7.setText(_translate("MainWindow", "Inhand Owner"))
		self.label_8.setText(_translate("MainWindow", "Transmission Type"))
		self.getprice_b.setText(_translate("MainWindow", "GET PRICE"))
		self.label_9.setText(_translate("MainWindow", "CAR RESALE PRICE PREDICTOR"))
		self.connect.setText(_translate("MainWindow", "GET"))
		self.exit_b.setText(_translate("MainWindow", "EXIT"))
		self.label_10.setText(_translate("MainWindow", "GET     - Redirects to browser"))
		self.label_11.setText(_translate("MainWindow", "MODEL - Choose the Machine Learning Model"))
		self.label_12.setText(_translate("MainWindow", "CONFIG - Choose the Configuration File"))

		#self.pickle_b.clicked.connect(self.choose_pickle)
		#self.config_b.clicked.connect(self.choose_config)
		#self.getprice_b.clicked.connect(self.getprice)


class Res(QMainWindow, Ui_MainWindow):
	def __init__(self,parent = None):
		super(Res,self).__init__(parent)


	def choose_pickle(self):
		pname = QFileDialog.getExistingDirectory(self, 'Select Folder')
		if pname!="":
				t1=threading.Thread(target=self.loadpickle,args=(pname,))
				t1.start()
		
	def loadpickle(self,pname):	
		global mymodel,mymodel1,mymodel2
		mymodel = pickle.load(open(pname+"\\abr.sav", 'rb'))
		mymodel1=pickle.load(open(pname+"\\xg.sav",'rb'))
		mymodel2=pickle.load(open(pname+"\\rfr.sav",'rb'))
		

	def choose_config(self):
		cname = QFileDialog.getOpenFileName(self, "Open File","","All Files (*)")
		if cname[0]!="":
				t1=threading.Thread(target=self.loadconfig, args=(cname[0],))
				t1.start()
	def exit_f(self):
		sys.exit()
	
	def open_url(self):
		import webbrowser
		url = "https://colab.research.google.com/github/varunpanchal283/Major-Project/blob/main/Car_Resale_Price_Prediction.ipynb"
		webbrowser.open(url, new=0, autoraise=True)

	def loadconfig(self,cname):
		global config
		config=configparser.ConfigParser()
		config.read(cname)
		self.brand_c.addItems([i for i in config["Brand"]])
		self.model_c.addItems([i for i in config["Model"]])
		self.engine_c.addItems([i for i in config["Automan"]])
		self.fuel_c.addItems([i for i in config["Engine Type"]])
		self.place_c.addItems([i for i in config["Place"]])
		self.year_c.addItems([i for i in config['Year']])
		self.owner_c.addItems([i for i in config['Inhand']])

	def getprice(self):
		global mymodel,config,mymodel2,mymodel1
		x=mymodel.predict([[int(config["Brand"][self.brand_c.currentText()]),
							int(config["Model"][self.model_c.currentText()]),
							int(config["Place"][self.place_c.currentText()]),
							int(config["Engine Type"][self.fuel_c.currentText()]),
							int(config["Year"][self.year_c.currentText()]),
							int(self.milage_c.text()),
							int(config["Inhand"][self.owner_c.currentText()]),
							int(config["Automan"][self.engine_c.currentText()])]])
		l=[[int(config["Brand"][self.brand_c.currentText()]),
							int(config["Model"][self.model_c.currentText()]),
							int(config["Place"][self.place_c.currentText()]),
							int(config["Engine Type"][self.fuel_c.currentText()]),
							int(config["Year"][self.year_c.currentText()]),
							int(self.milage_c.text()),
							int(config["Inhand"][self.owner_c.currentText()]),
							int(config["Automan"][self.engine_c.currentText()])]]
		y=mymodel1.predict(l)
		z=mymodel2.predict(l)
		res=(int(x[0])+int(y[0])+int(z[0]))//3
		res="{:.1f}".format(res/100000)
		self.result.setText("Predicted Price is Rs."+res+" Lakhs")



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Res()
	ui.setupUi(MainWindow)
	MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	MainWindow.show()
	sys.exit(app.exec_())
