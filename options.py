from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionWindow(object):
    def setupUi(self, OptionWindow):
        OptionWindow.setObjectName("OptionWindow")
        OptionWindow.resize(737, 596)
        font = QtGui.QFont()
        font.setPointSize(4)
        OptionWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(OptionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MapScreenBotton = QtWidgets.QPushButton(self.centralwidget)
        self.MapScreenBotton.setGeometry(QtCore.QRect(160, 160, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MapScreenBotton.setFont(font)
        self.MapScreenBotton.setObjectName("MapScreenBotton")
        self.HTMLBotton = QtWidgets.QPushButton(self.centralwidget)
        self.HTMLBotton.setGeometry(QtCore.QRect(160, 370, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.HTMLBotton.setFont(font)
        self.HTMLBotton.setObjectName("HTMLBotton")
        OptionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptionWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionWindow)

    def retranslateUi(self, OptionWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionWindow.setWindowTitle(_translate("OptionWindow", "Interactibe Map -Options"))
        self.MapScreenBotton.setText(_translate("OptionWindow", "Get Event Informatiion"))
        self.HTMLBotton.setText(_translate("OptionWindow", "Create HTML file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionWindow = QtWidgets.QMainWindow()
    ui = Ui_OptionWindow()
    ui.setupUi(OptionWindow)
    OptionWindow.show()
    sys.exit(app.exec_())
