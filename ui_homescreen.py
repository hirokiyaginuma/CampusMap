import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mapscreen import Ui_MapScreen


class Ui_HomeScreen(object):
    def __init__(self):
        self.mapfilepath_ = os.getcwd() + '\\mapfile'

    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(800, 900)
        self.centralwidget = QtWidgets.QWidget(HomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 680, 591, 151))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 40, 681, 231))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "\\img\\UTTylerLogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 310, 311, 311))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 310, 311, 311))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 280, 671, 61))
        self.label_4.setObjectName("label_4")
        HomeScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HomeScreen)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        HomeScreen.setStatusBar(self.statusbar)

        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

        self.pushButton.clicked.connect(self.openMap)

    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "HomeScreen"))
        self.pushButton.setText(_translate("HomeScreen", "Launch Map"))
        self.label_2.setText(_translate("HomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Current Event</span></p></body></html>"))
        self.label_3.setText(_translate("HomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Weather Forecast</span></p></body></html>"))
        self.label_4.setText(_translate("HomeScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Campus Map</span></p></body></html>"))

    def openMap(self):
        self.MapScreen = QtWidgets.QMainWindow()
        self.ui = Ui_MapScreen()
        self.ui.setupUi(self.MapScreen)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    HomeScreen = QtWidgets.QMainWindow()
    ui = Ui_HomeScreen()
    ui.setupUi(HomeScreen)
    HomeScreen.show()
    sys.exit(app.exec_())