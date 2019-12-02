from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLable = QtWidgets.QLabel(self.centralwidget)
        self.titleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLable.setObjectName("titleLable")
        self.verticalLayout_2.addWidget(self.titleLable)
        self.titleImage = QtWidgets.QLabel(self.centralwidget)
        self.titleImage.setText("")
        self.titleImage.setPixmap(QtGui.QPixmap("mapfile/img/title.png"))
        self.titleImage.setAlignment(QtCore.Qt.AlignCenter)
        self.titleImage.setObjectName("titleImage")
        self.verticalLayout_2.addWidget(self.titleImage)
        self.HomeScreenBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.HomeScreenBotton.setFont(font)
        self.HomeScreenBotton.setObjectName("HomeScreenBotton")
        self.verticalLayout_2.addWidget(self.HomeScreenBotton)
        self.OptionsBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.OptionsBotton.setFont(font)
        self.OptionsBotton.setObjectName("OptionsBotton")
        self.verticalLayout_2.addWidget(self.OptionsBotton)
        WelcomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "Interactive Map - Welcome"))
        self.titleLable.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">UT Tyler Interactive Campus Map</span></p></body></html>"))
        self.HomeScreenBotton.setText(_translate("WelcomeWindow", "Launch Home Screen"))
        self.OptionsBotton.setText(_translate("WelcomeWindow", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec_())
