import sys
from PyQt5 import QtWidgets
from welcome import Ui_WelcomeWindow
from options import Ui_OptionWindow
from HomeScreen import Ui_HomeScreen
from MapScreen import Ui_MapScreen
from mapConstructor import MapConstructor
from event import Event
from webServer import WebServer


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
        event = Event()
        event.getEvent()
        event.downloadImage()
        print("Event created.")

    def HTML(self):
        self.map = MapConstructor()
        self.map.createMap()


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
