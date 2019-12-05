import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_MapScreen(object):
    def __init__(self):
        self.maphtmlpath_ = os.getcwd() + '\\mapfile\\map\\events.html'
        self.path_ = "http://localhost:8080/map/events.html"


    def setupUi(self, MapScreen):
        MapScreen.setObjectName("MapScreen")
        MapScreen.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MapScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.HomeScreenBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HomeScreenBotton.setFont(font)
        self.HomeScreenBotton.setObjectName("HomeScreenBotton")
        self.verticalLayout_2.addWidget(self.HomeScreenBotton)
        self.MapLayout = QtWidgets.QVBoxLayout()
        self.MapLayout.setSpacing(0)
        self.MapLayout.setObjectName("MapLayout")
        self.verticalLayout_2.addLayout(self.MapLayout)
        MapScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MapScreen)
        QtCore.QMetaObject.connectSlotsByName(MapScreen)

        self.web = QWebEngineView()
        self.web.page().profile().clearHttpCache()
        # self.url = QtCore.QUrl.fromLocalFile(self.maphtmlpath_)
        self.url = QtCore.QUrl(self.path_)
        self.web.load(self.url)

        self.MapLayout.addWidget(self.web)



    def retranslateUi(self, MapScreen):
        _translate = QtCore.QCoreApplication.translate
        MapScreen.setWindowTitle(_translate("MapScreen", "Interactive Map - Map Screen"))
        self.HomeScreenBotton.setText(_translate("MapScreen", "Home Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MapScreen = QtWidgets.QMainWindow()
    ui = Ui_MapScreen()
    ui.setupUi(MapScreen)
    MapScreen.showFullScreen()
    sys.exit(app.exec_())
