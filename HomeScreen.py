import os
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from weather import Weather
from event import Event


class Ui_HomeScreen(object):
    def __init__(self):
        self.mapfilepath_ = os.getcwd() + '\\mapfile'
        self.getDate()
        self.getWeather()
        self.getEvent()

    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(1280, 720)
        HomeScreen.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.centralwidget = QtWidgets.QWidget(HomeScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.UTLogoLayout = QtWidgets.QHBoxLayout()
        self.UTLogoLayout.setObjectName("UTLogoLayout")
        self.UTLogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.UTLogoLabel.setText("")
        self.UTLogoLabel.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "\\img\\UTTylerLogo.png")) ##
        self.UTLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UTLogoLabel.setObjectName("UTLogoLabel")
        self.UTLogoLayout.addWidget(self.UTLogoLabel)
        self.gridLayout_2.addLayout(self.UTLogoLayout, 1, 2, 1, 3)
        self.BottonLayout = QtWidgets.QVBoxLayout()
        self.BottonLayout.setObjectName("BottonLayout")
        self.launchMapBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.launchMapBotton.setFont(font)
        self.launchMapBotton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.launchMapBotton.setObjectName("launchMapBotton")
        self.BottonLayout.addWidget(self.launchMapBotton)
        self.gridLayout_2.addLayout(self.BottonLayout, 3, 3, 1, 1)
        self.WeatherLayout = QtWidgets.QVBoxLayout()
        self.WeatherLayout.setObjectName("WeatherLayout")
        self.WeatherLabel = QtWidgets.QLabel(self.centralwidget)
        self.WeatherLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherLabel.setObjectName("WeatherLabel")
        self.WeatherLayout.addWidget(self.WeatherLabel)
        self.weatherIconLayout = QtWidgets.QHBoxLayout()
        self.weatherIconLayout.setObjectName("weatherIconLayout")
        self.weatherIconLabel = QtWidgets.QLabel(self.centralwidget)
        self.weatherIconLabel.setStyleSheet("")
        self.weatherIconLabel.setText("")
        self.weatherIconLabel.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/weatherIcon/" + self.weather_icon + ".png")) ##
        self.weatherIconLabel.setObjectName("weatherIconLabel")
        self.weatherIconLayout.addWidget(self.weatherIconLabel)
        self.weatherGeneral = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.weatherGeneral.setFont(font)
        self.weatherGeneral.setObjectName("weatherGeneral")
        self.weatherIconLayout.addWidget(self.weatherGeneral)
        self.WeatherLayout.addLayout(self.weatherIconLayout)
        self.weatherDescription = QtWidgets.QLabel(self.centralwidget)
        self.weatherDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherDescription.setObjectName("weatherDescription")
        self.WeatherLayout.addWidget(self.weatherDescription)
        self.weatherTemperature = QtWidgets.QLabel(self.centralwidget)
        self.weatherTemperature.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherTemperature.setObjectName("weatherTemperature")
        self.WeatherLayout.addWidget(self.weatherTemperature)
        self.weatherPressure = QtWidgets.QLabel(self.centralwidget)
        self.weatherPressure.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherPressure.setObjectName("weatherPressure")
        self.WeatherLayout.addWidget(self.weatherPressure)
        self.weatherHumidity = QtWidgets.QLabel(self.centralwidget)
        self.weatherHumidity.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherHumidity.setObjectName("weatherHumidity")
        self.WeatherLayout.addWidget(self.weatherHumidity)
        self.gridLayout_2.addLayout(self.WeatherLayout, 2, 4, 2, 1)
        self.EventLayout = QtWidgets.QVBoxLayout()
        self.EventLayout.setObjectName("EventLayout")
        self.eventLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventLabel.setObjectName("eventLabel")
        self.EventLayout.addWidget(self.eventLabel)
        self.eventImage = QtWidgets.QLabel(self.centralwidget)
        self.eventImage.setText("")
        # self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/eventimage/0.jpg")) ##
        self.eventImage.setAlignment(QtCore.Qt.AlignCenter)
        self.eventImage.setObjectName("eventImage")
        self.EventLayout.addWidget(self.eventImage)
        self.eventName = QtWidgets.QLabel(self.centralwidget)
        self.eventName.setAlignment(QtCore.Qt.AlignCenter)
        self.eventName.setObjectName("eventName")
        self.EventLayout.addWidget(self.eventName)
        self.eventLocation = QtWidgets.QLabel(self.centralwidget)
        self.eventLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.eventLocation.setObjectName("eventLocation")
        self.EventLayout.addWidget(self.eventLocation)
        self.eventTime = QtWidgets.QLabel(self.centralwidget)
        self.eventTime.setAlignment(QtCore.Qt.AlignCenter)
        self.eventTime.setObjectName("eventTime")
        self.EventLayout.addWidget(self.eventTime)
        self.EventBotton = QtWidgets.QHBoxLayout()
        self.EventBotton.setObjectName("EventBotton")
        self.previousBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.previousBotton.setFont(font)
        self.previousBotton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.previousBotton.setObjectName("previousBotton")
        self.EventBotton.addWidget(self.previousBotton)
        self.nextBotton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nextBotton.setFont(font)
        self.nextBotton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nextBotton.setObjectName("nextBotton")
        self.EventBotton.addWidget(self.nextBotton)
        self.EventLayout.addLayout(self.EventBotton)
        self.gridLayout_2.addLayout(self.EventLayout, 2, 2, 2, 1)
        self.DateLayout = QtWidgets.QVBoxLayout()
        self.DateLayout.setObjectName("DateLayout")
        self.CampusMap = QtWidgets.QLabel(self.centralwidget)
        self.CampusMap.setAlignment(QtCore.Qt.AlignCenter)
        self.CampusMap.setObjectName("CampusMap")
        self.DateLayout.addWidget(self.CampusMap)
        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Date.setObjectName("Date")
        self.DateLayout.addWidget(self.Date)
        self.gridLayout_2.addLayout(self.DateLayout, 2, 3, 1, 1)
        HomeScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

        self.nextBotton.clicked.connect(self.eventNext)
        self.previousBotton.clicked.connect(self.eventPrevious)

        try:
            image = open(self.mapfilepath_ + "/eventimage/0.jpg")
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/eventimage/0.jpg"))  ##
        except IOError:
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/img/UTsquarelogo.png"))


    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "Interactive Map - Home Screen"))
        self.launchMapBotton.setText(_translate("HomeScreen", "Launch Map"))
        self.WeatherLabel.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-size:16pt;\">Weather</span></p></body></html>"))
        self.weatherGeneral.setText(_translate("HomeScreen", self.weather_main_str))
        self.weatherDescription.setText(_translate("HomeScreen", self.weather_des_str))
        self.weatherTemperature.setText(_translate("HomeScreen", self.weather_tem_str))
        self.weatherPressure.setText(_translate("HomeScreen", self.weather_pressure_str))
        self.weatherHumidity.setText(_translate("HomeScreen", self.weather_humidity_str))
        self.eventLabel.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-size:16pt;\">Campus Events</span></p></body></html>"))
        self.eventName.setText(_translate("HomeScreen", self.event_name_str))
        self.eventLocation.setText(_translate("HomeScreen", self.event_location_str))
        self.eventTime.setText(_translate("HomeScreen", self.event_date_str))
        self.previousBotton.setText(_translate("HomeScreen", "Previous Event"))
        self.nextBotton.setText(_translate("HomeScreen", "Next Event"))
        self.CampusMap.setText(_translate("HomeScreen", "<html><head/><body><p><span style=\" font-size:36pt;\">Campus Map</span></p></body></html>"))
        self.Date.setText(_translate("HomeScreen", self.date_str))

    def getDate(self):
        self.today = date.today()
        self.today_format = self.today.strftime("%m/%d/%Y")
        self.date_str = "<html><head/><body><p><span style=\" font-size:48pt;\">" + str(self.today_format) + "</span></p></body></html>"

    def getWeather(self):
        self.weather = Weather()
        self.weather_main_str = "<html><head/><body><p><span style=\" font-size:20pt;\">" + str(
            self.weather.getWeatherMain()) + "</span></p></body></html>"
        self.weather_des_str = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Weather: " + str(
            self.weather.getDescription()) + "</span></p></body></html>"
        self.weather_tem_str = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Temperature: " + str(
            self.weather.getCTemperature()) + "(C)/" + str(
            self.weather.getFTemperature()) + "(F)</span></p></body></html>"
        self.weather_pressure_str = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Pressure: " + str(
            self.weather.getPressure()) + " (hPa)</span></p></body></html>"
        self.weather_humidity_str = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Humidity: " + str(
            self.weather.getHumidity()) + "%</span></p></body></html>"
        self.weather_icon = self.weather.getIcon()

    def getEvent(self):
        self.event = Event()
        self.event.readList()
        self.eventCounter = 0
        self.event_name_str = "<html><head/><body><p><span style=\" font-size:16pt;\">" + self.event.eventName[
            self.eventCounter] + "</span></p></body></html>"
        self.event_location_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Location: " + self.event.eventLocation[
            self.eventCounter] + "</span></p></body></html>"
        self.event_date_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Date: " + self.event.eventDate[
            self.eventCounter] + "</span></p></body></html>"

    def eventNext(self):
        _translate = QtCore.QCoreApplication.translate

        if self.eventCounter == 14:
            self.eventCounter = 0
        else:
            self.eventCounter = self.eventCounter + 1

        self.event_name_str = "<html><head/><body><p><span style=\" font-size:16pt;\">" + self.event.eventName[
            self.eventCounter] + "</span></p></body></html>"
        self.event_location_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Location: " + \
                                  self.event.eventLocation[self.eventCounter] + "</span></p></body></html>"
        self.event_date_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Date: " + self.event.eventDate[
            self.eventCounter] + "</span></p></body></html>"
        self.eventName.setText(_translate("HomeScreen", self.event_name_str))
        self.eventLocation.setText(_translate("HomeScreen", self.event_location_str))
        self.eventTime.setText(_translate("HomeScreen", self.event_date_str))

        self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/eventimage/" + str(self.eventCounter) + ".jpg"))

        try:
            image = open(self.mapfilepath_ + "/eventimage/" + str(self.eventCounter) + ".jpg")
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/eventimage/" + str(self.eventCounter) + ".jpg"))
        except IOError:
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/img/UTsquarelogo.png"))

    def eventPrevious(self):
        _translate = QtCore.QCoreApplication.translate

        if self.eventCounter == 0:
            self.eventCounter = 14
        else:
            self.eventCounter = self.eventCounter - 1

        self.event_name_str = "<html><head/><body><p><span style=\" font-size:16pt;\">" + self.event.eventName[
            self.eventCounter] + "</span></p></body></html>"
        self.event_location_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Location: " + \
                                  self.event.eventLocation[self.eventCounter] + "</span></p></body></html>"
        self.event_date_str = "<html><head/><body><p><span style=\" font-size:16pt;\">Date: " + self.event.eventDate[
            self.eventCounter] + "</span></p></body></html>"
        self.eventName.setText(_translate("HomeScreen", self.event_name_str))
        self.eventLocation.setText(_translate("HomeScreen", self.event_location_str))
        self.eventTime.setText(_translate("HomeScreen", self.event_date_str))

        try:
            image = open(self.mapfilepath_ + "/eventimage/" + str(self.eventCounter) + ".jpg")
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/eventimage/" + str(self.eventCounter) + ".jpg"))
        except IOError:
            self.eventImage.setPixmap(QtGui.QPixmap(self.mapfilepath_ + "/img/UTsquarelogo.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeScreen = QtWidgets.QMainWindow()
    ui = Ui_HomeScreen()
    ui.setupUi(HomeScreen)
    HomeScreen.show()
    sys.exit(app.exec_())
