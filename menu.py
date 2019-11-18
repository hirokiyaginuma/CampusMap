import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from mapConstructor import MapConstructor
from ui_homescreen import Ui_HomeScreen
from ui_mapscreen import Ui_MapScreen
from eventDemo import Ui_DemoScreen


class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        DebugWindow.setObjectName("DebugWindow")
        DebugWindow.resize(737, 596)
        font = QtGui.QFont()
        font.setPointSize(4)
        DebugWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(DebugWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 230, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 350, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 460, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        DebugWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DebugWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        DebugWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DebugWindow)
        self.statusbar.setObjectName("statusbar")
        DebugWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DebugWindow)
        QtCore.QMetaObject.connectSlotsByName(DebugWindow)

        self.pushButton.clicked.connect(self.homeScreen)
        self.pushButton_2.clicked.connect(self.mapScreen)
        self.pushButton_3.clicked.connect(self.createMapHTML)
        self.pushButton_4.clicked.connect(self.demoScreen)

    def retranslateUi(self, DebugWindow):
        _translate = QtCore.QCoreApplication.translate
        DebugWindow.setWindowTitle(_translate("DebugWindow", "DebugMenu"))
        self.pushButton.setText(_translate("DebugWindow", "Home Screen"))
        self.pushButton_2.setText(_translate("DebugWindow", "Map Screen"))
        self.pushButton_3.setText(_translate("DebugWindow", "Create HTML file"))
        self.pushButton_4.setText(_translate("DebugWindow", "Event Demo"))

    def homeScreen(self):
        self.HomeScreen = QtWidgets.QMainWindow()
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self.HomeScreen)
        self.HomeScreen.show()

    def mapScreen(self):
        self.MapScreen = QtWidgets.QMainWindow()
        self.ui = Ui_MapScreen()
        self.ui.setupUi(self.MapScreen)

    def createMapHTML(self):
        self.map = MapConstructor()
        self.map.createMap()

    def demoScreen(self):
        self.DemoScreen = QtWidgets.QMainWindow()
        self.ui = Ui_DemoScreen()
        self.ui.setupUi(self.DemoScreen)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DebugWindow = QtWidgets.QMainWindow()
    ui = Ui_DebugWindow()
    ui.setupUi(DebugWindow)
    DebugWindow.show()
    sys.exit(app.exec_())