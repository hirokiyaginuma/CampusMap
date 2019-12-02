import requests, pprint


class Weather(object):
    def __init__(self):
        self.temperature = 0
        self.Ctemperature = 0
        self.Ftemperature = 0
        self.pressure = 0
        self.humidity = 0
        self.weather_main = ""
        self.weather_description = ""
        self.icon = ""
        self.weatherJSON = None
        self.getWeatherinfo()

    @staticmethod
    def kelvinToCelsius(kelvin):
        return round(kelvin - 273.15, 2)

    @staticmethod
    def kelvinToFahrenheit(kelvin):
        return round(kelvin * 9/5 - 459.67, 2)

    def getTemperature(self):
        return self.temperature

    def getCTemperature(self):
        return self.Ctemperature

    def getFTemperature(self):
        return self.Ftemperature

    def getPressure(self):
        return self.pressure

    def getHumidity(self):
        return self.humidity

    def getWeatherMain(self):
        return self.weather_main

    def getDescription(self):
        return self.weather_description

    def getIcon(self):
        return self.icon

    def getWeatherinfo(self):
        api_key = "ffc0168a8604bce317b2e4fae05572ed"
        openWeatherMap_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Tyler"

        url = openWeatherMap_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(url)

        self.weatherJSON = response.json()

        if (self.weatherJSON["cod"] != "404") or (self.weatherJSON["cod"] != "401") or (self.weatherJSON["cod"] != "429"):
            x = self.weatherJSON["main"]
            self.temperature = x["temp"]
            self.Ctemperature = self.kelvinToCelsius(self.temperature)
            self.Ftemperature = self.kelvinToFahrenheit(self.temperature)
            self.pressure = x["pressure"]
            self.humidity = x["humidity"]
            y = self.weatherJSON["weather"]
            self.weather_main = y[0]["main"]
            self.weather_description = y[0]["description"]
            self.icon = y[0]["icon"]
        else:
            print("Error: Could not get weather information")

    def pprintJson(self):
        pprint.pprint(self.weatherJSON)
        print()

    def printWeatherinfo(self):
        print(" Temperature (in kelvin unit) = " +
              str(self.temperature) +
              "\n Temperature (in celsius unit) = " +
              str(self.Ctemperature) +
              "\n Temperature (in fahrenheit unit) = " +
              str(self.Ftemperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(self.pressure) +
              "\n humidity (in percentage) = " +
              str(self.humidity) +
              "\n main = " +
              str(self.weather_main) +
              "\n description = " +
              str(self.weather_description))

if __name__ == '__main__':
    weather = Weather()
    weather.pprintJson()
    #weather.printWeatherinfo()
