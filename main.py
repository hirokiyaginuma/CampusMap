import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_DebugWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    DebugWindow = QtWidgets.QMainWindow()
    ui = Ui_DebugWindow()
    ui.setupUi(DebugWindow)
    DebugWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
