import os
import folium
import csv

from folium import FeatureGroup, LayerControl, Map, Marker

class MapConstructor:
    def __init__(self):
        self.temp = 0
        self.mapfilepath_ = os.getcwd() + '\\mapfile'

    def getMapPath(self):
        return self.mapfilepath_ + '\\map.html'

    def createMap(self):
        # UT lat, lon
        UTTCoords = (32.3158, -95.2544)

        #The idea will be to read in from the file the room numbers and assign them to the appropriate building.
        #I will also link the building code to the building to begin building the basic search functionality.

        filePath = 'mapfile/roomList/roomList.csv'
        with open(filePath) as roomListFile:
            roomList = csv.reader(roomListFile, delimiter=',')

            buildCodes = []
            roomNum = []
            roomType = []
            roomFloor = []

            for row in roomList:
                buildCodes.append(row[0])
                roomNum.append(row[1].lstrip('0'))
                roomType.append(row[2])
                roomFloor.append(row[1].lstrip('0')[0])



        # Create map object
        UTmap = folium.Map(location=UTTCoords, zoom_start=16, tiles="OpenStreetMap", min_zoom=16, min_lat=32.309790,
                           max_lat=32.32124, min_lon=-95.239071, max_lon=-95.260618, max_bounds=True, zoom_control=True)

        hereTxt = folium.Html('You are here!', script=True)
        hereWindow = folium.Popup(hereTxt, max_width=300)
        hereIcon = folium.Icon(color='red', icon='info-sign')
        folium.Marker(location=[32.315950, -95.252574], popup=hereWindow, icon=hereIcon).add_to(UTmap)

        #
        # #Interactive Map location
        # folium.Marker(location=[32.315950,-95.252574], tooltip='You are here', color='black', fill_color='Yellow', fill_opacity=1).add_to(UTmap)


        floorListOverlay = FeatureGroup(name="Floor List")


        # Adding buildings
        folium.LayerControl().add_to(UTmap)

        # Orneleas Residence Hall
        folium.CircleMarker(location=[32.314358, -95.251427], tooltip='Ornelas Residence Hall',
                            radius=10, color='black', weight=1, fill_color='Orange', fill_opacity=0.5,
                            fill=True).add_to(UTmap)

        # This is the first version. Here for reference.
        # Soules College of Business and Technology
        # folium.CircleMarker(location=[32.313234,-95.251733], tooltip='Soules College of Business and Technology',
        #                        radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.5, fill=True, ).add_to(UTmap)



        #okay, check each building code and match it to the building name. Then take the roomNum at the same index
        #and put it in a list of the correct floor

        COBFloor1 = 'Floor 1:<br><br>'
        COBFloor2 = 'Floor 2:<br><br>'
        COBFloor3 = 'Floor 3:<br><br>'

        for i, build in enumerate(buildCodes):
            if build == 'COB' and roomFloor[i] == '1':
                COBFloor1 += '<nbsp>Room Number: ' + roomNum[i] + '&nbsp;&nbsp;&nbsp;&nbsp;' + 'Type: ' + roomType[i] + '<br>'
            elif build == 'COB' and roomFloor[i] == '2':
                COBFloor2 += 'Room Number: ' + roomNum[i] + '&nbsp;&nbsp;&nbsp;&nbsp;' + 'Type: ' + roomType[i] + '<br>'
            elif build == 'COB' and roomFloor[i] == '3':
                COBFloor3 += 'Room Number: ' + roomNum[i] + '&nbsp;&nbsp;&nbsp;&nbsp;' + 'Type: ' + roomType[i] + '<br>'

        COBhtml = """
            <h1>SOULES COLLEGE OF BUSINESS</h1><br>
            <p>""" + COBFloor1 + "<br><br>" + COBFloor2 + "<br><br>" + COBFloor3 + "<br><br>" + """
            </p>
            """


        soulesTxt = folium.Html(COBhtml,
                                script=True)

        soulesWindow = folium.Popup(html=soulesTxt, min_width=400, max_width=900, max_height=300, parse_html=True)
        soulesIcon = folium.Icon(color='purple', icon='star')

        # Clickable marker
        COB = folium.CircleMarker(location=[32.313234, -95.251733], tooltip='Soules College of Business and Technology',
                            radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.5, fill=True,
                            popup=soulesWindow)
        COB.add_to(UTmap)


        # This isn't really what we want to do, more just a proof of concept. We need to get an API key from OpenWeather and
        # then display the current weather in a window that is in a fixed location on the window of the screen (eg. upper right)
        weatherLink = folium.Html('<a href=https://openweathermap.org/city/4738214>Current Weather</a>', script=True)
        weatherIcon = folium.Icon(color='blue', icon='cloud')
        weatherWindow = folium.Popup(weatherLink, max_width=300)
        folium.Marker(location=[32.3158, -95.2544], tooltip='Weather', icon=weatherIcon, popup=weatherWindow).add_to(UTmap)


        UTmap.save(self.getMapPath())
        print('HTML file created at '+ self.getMapPath())

if __name__ == '__main__':
    map = MapConstructor()
    map.createMap()