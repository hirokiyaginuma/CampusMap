import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_DemoScreen(object):
    def __init__(self):
        self.mapfilepath_ = os.getcwd() + '\\mapfile\\eventDemo\\events.html'

    def setupUi(self, DemoScreen):
        self.win = QWidget()
        self.win.setWindowTitle('Interactive Map - Demo Screen')

        self.layout = QVBoxLayout()
        self.win.setLayout(self.layout)

        self.web = QWebEngineView()
        self.url = QtCore.QUrl.fromLocalFile(self.mapfilepath_)
        self.web.load(self.url)

        self.layout.addWidget(self.web)

        self.win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MapScreen = QtWidgets.QMainWindow()
    ui = Ui_DemoScreen()
    ui.setupUi(MapScreen)
    sys.exit(app.exec_())