import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_MapScreen(object):
    def __init__(self):
        self.mapfilepath_ = os.getcwd() + '\\mapfile\\map.html'

    def setupUi(self, MapScreen):
        # keep this block of code for future use

        """MapScreen.setObjectName("MapScreen")
        MapScreen.resize(1117, 898)
        self.centralwidget = QtWidgets.QWidget(MapScreen)
        self.centralwidget.setObjectName("centralwidget")
        MapScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        MapScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MapScreen)
        self.statusbar.setObjectName("statusbar")
        MapScreen.setStatusBar(self.statusbar)

        self.retranslateUi(MapScreen)
        QtCore.QMetaObject.connectSlotsByName(MapScreen)"""

        self.win = QWidget()
        self.win.setWindowTitle('Interactive Map - Map Screen')

        self.layout = QVBoxLayout()
        self.win.setLayout(self.layout)

        self.web = QWebEngineView()
        self.url = QtCore.QUrl.fromLocalFile(self.mapfilepath_)
        self.web.load(self.url)

        self.layout.addWidget(self.web)

        self.win.show()

    def retranslateUi(self, MapScreen): # currently not be used
        _translate = QtCore.QCoreApplication.translate
        MapScreen.setWindowTitle(_translate("MapScreen", "MapScreen"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MapScreen = QtWidgets.QMainWindow()
    ui = Ui_MapScreen()
    ui.setupUi(MapScreen)
    #MapScreen.show()
    sys.exit(app.exec_())