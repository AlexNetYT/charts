# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(object):
    def setMetar(self,text):
        self.metar_label.setText(text)
    def getID(self, sel_icao):
        if sel_icao != 'AIP':
            print(sel_icao)
            main.MainWindow.icao = sel_icao
            main.MainWindow.main_page = False
            main.MainWindow.GetMetar(ICAO=sel_icao,self=self)
        else:
            main.MainWindow.main_page = True
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 165, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UUEE = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UUEE.setMinimumSize(QtCore.QSize(0, 65))
        self.UUEE.setObjectName("UUEE")
        self.verticalLayout.addWidget(self.UUEE)
        self.UUWW = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UUWW.setMinimumSize(QtCore.QSize(0, 65))
        self.UUWW.setObjectName("UUWW")
        self.verticalLayout.addWidget(self.UUWW)
        self.ULLI = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ULLI.setMinimumSize(QtCore.QSize(0, 65))
        self.ULLI.setObjectName("ULLI")
        self.verticalLayout.addWidget(self.ULLI)
        self.UWGG = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UWGG.setMinimumSize(QtCore.QSize(0, 65))
        self.UWGG.setObjectName("UWGG")
        self.verticalLayout.addWidget(self.UWGG)
        self.UWKD = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UWKD.setMinimumSize(QtCore.QSize(0, 65))
        self.UWKD.setObjectName("UWKD")
        self.verticalLayout.addWidget(self.UWKD)
        self.EFHK = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EFHK.setMinimumSize(QtCore.QSize(0, 65))
        self.EFHK.setObjectName("EFHK")
        self.verticalLayout.addWidget(self.EFHK)
        self.URSS = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.URSS.setMinimumSize(QtCore.QSize(0, 65))
        self.URSS.setObjectName("URSS")
        self.verticalLayout.addWidget(self.URSS)
        self.URKA = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.URKA.setMinimumSize(QtCore.QSize(0, 65))
        self.URKA.setObjectName("URKA")
        self.verticalLayout.addWidget(self.URKA)
        self.UMKK = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UMKK.setMinimumSize(QtCore.QSize(0, 65))
        self.UMKK.setObjectName("UMKK")
        self.verticalLayout.addWidget(self.UMKK)
        self.AIP = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AIP.setMinimumSize(QtCore.QSize(0, 65))
        self.AIP.setObjectName("AIP")
        self.verticalLayout.addWidget(self.AIP)
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        
        # self.webview = WebEngineView(self) # self must have - ???????????????? ?????????????? ???????? ?? ???????????????? ?????????????????? ????????????????
        # self.webview.setGeometry(QtCore.QRect(165, 31, 921, 641))
        # self.webview.setObjectName("graphicsView")
        # self.webview.load(QUrl("http://www.baidu.com"))

        self.metar_label = QtWidgets.QLabel(self.centralwidget)
        self.metar_label.setGeometry(QtCore.QRect(180, 0, 901, 31))
        self.metar_label.setObjectName("metar_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UUEE.setText(_translate("MainWindow", "UUEE"))
        self.UUWW.setText(_translate("MainWindow", "UUWW"))
        self.ULLI.setText(_translate("MainWindow", "ULLI"))
        self.UWGG.setText(_translate("MainWindow", "UWGG"))
        self.UWKD.setText(_translate("MainWindow", "UWKD"))
        self.EFHK.setText(_translate("MainWindow", "EFHK"))
        self.URSS.setText(_translate("MainWindow", "URSS"))
        self.URKA.setText(_translate("MainWindow", "URKA"))
        self.UMKK.setText(_translate("MainWindow", "UMMK"))
        self.AIP.setText(_translate("MainWindow", "??????"))
        self.UUEE.clicked.connect(lambda x: self.getID(self.UUEE.text()))
        self.UUWW.clicked.connect(lambda x: self.getID(self.UUWW.text()))
        self.ULLI.clicked.connect(lambda x: self.getID(self.ULLI.text()))
        self.UWGG.clicked.connect(lambda x: self.getID(self.UWGG.text()))
        self.UWKD.clicked.connect(lambda x: self.getID(self.UWKD.text()))
        self.EFHK.clicked.connect(lambda x: self.getID(self.EFHK.text()))
        self.URSS.clicked.connect(lambda x: self.getID(self.URSS.text()))
        self.URKA.clicked.connect(lambda x: self.getID(self.URKA.text()))
        self.UMKK.clicked.connect(lambda x: self.getID(self.UMKK.text()))
        self.AIP.clicked.connect(lambda x: self.getID("AIP"))
        self.metar_label.setText(_translate("MainWindow", "METAR: "
"\n"
""))
