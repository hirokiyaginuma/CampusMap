import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from welcome import Ui_WelcomeWindow
from options import Ui_OptionWindow
from HomeScreen import Ui_HomeScreen
from MapScreen import Ui_MapScreen
from mapConstructor import MapConstructor
from event import Event
from webServer import WebServer


class Dialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 301, 71))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.OKBotton)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate(
            "Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Events are successfully updated</span></p></body></html>"))

    def OKBotton(self):
        self.hide()


class Dialog2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 301, 71))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.OKBotton)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate(
            "Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Maps are successfully updated</span></p></body></html>"))

    def OKBotton(self):
        self.hide()


class Welcome(QtWidgets.QMainWindow, Ui_WelcomeWindow):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.setupUi(self)
        self.HomeScreenBotton.clicked.connect(self.homeBotton)
        self.OptionsBotton.clicked.connect(self.optionsBotton)

    def homeBotton(self):
        self.homescreen = HomeScreen()
        self.homescreen.showFullScreen()
        self.hide()

    def optionsBotton(self):
        self.op = Options()
        self.op.show()


class Options(QtWidgets.QMainWindow, Ui_OptionWindow):
    def __init__(self, parent=None):
        super(Options, self).__init__(parent)
        self.setupUi(self)
        self.MapScreenBotton.clicked.connect(self.mapBotton)
        self.HTMLBotton.clicked.connect(self.HTML)

    def mapBotton(self):
        self.dialog = Dialog()
        event = Event()
        event.getEvent()
        event.downloadImage()
        self.map = MapConstructor()
        self.map.scriptEvent()
        self.dialog.show()

    def HTML(self):
        self.dialog = Dialog2()
        self.map = MapConstructor()
        self.map.createMap()
        self.map.scriptEvent()
        self.dialog.show()


class HomeScreen(QtWidgets.QMainWindow, Ui_HomeScreen):
    def __init__(self, parent=None):
        super(HomeScreen, self).__init__(parent)
        self.setupUi(self)
        self.launchMapBotton.clicked.connect(self.mapBotton)

    def mapBotton(self):
        self.mapscreen = MapScreen()
        self.mapscreen.showFullScreen()
        self.hide()


class MapScreen(QtWidgets.QMainWindow, Ui_MapScreen):
    def __init__(self, parent=None):
        super(MapScreen, self).__init__(parent)
        self.setupUi(self)
        self.HomeScreenBotton.clicked.connect(self.homeBotton)

    def homeBotton(self):
        self.homescreen = HomeScreen()
        self.hide()
        self.homescreen.showFullScreen()


if __name__ == '__main__':
    webserver = WebServer()
    webserver.startServer()
    app = QtWidgets.QApplication(sys.argv)
    w = Welcome()
    w.show()
    sys.exit(app.exec_())
