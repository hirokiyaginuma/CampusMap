import os
import folium
import csv
from bs4 import BeautifulSoup
from event import Event


class MapConstructor:
    def __init__(self):
        self.temp = 0
        self.mapfilepath_ = os.getcwd() + '\\mapfile\\map'

        # Lists of: building codes, room numbers, room types read directly from file.
        # Room floor list is extrapolated from first digit of room number
        self.buildCodes = []
        self.roomNum = []
        self.roomType = []
        self.roomFloor = []

        self.eventdivs = []

        # self.readEvent()

    def scriptEvent(self):
        event = Event()
        event.readList()

        with open(self.mapfilepath_ + '\\map.html') as map:
            text = map.read()
            self.soup = BeautifulSoup(text, 'lxml')

        eventScript = self.soup.find_all('script', id="eventvars")

        for script in eventScript:
            script.extract()

        new_link = self.soup.new_tag("script", id="eventvars")
        new_link.string = "\nvar names = " + str(event.eventName) + "; \nvar date = " + str(event.eventDate) + ";" + " \nvar locations = " + str(event.eventLocation) + ";"
        self.soup.body.append(new_link)

        with open(self.mapfilepath_ + '\\map.html', 'w') as map:
            map.write(str(self.soup))

    def getMapPath(self):
        return self.mapfilepath_ + '\\map.html'

    def getRoomFilePath(self):
        return self.mapfilepath_ + '\\roomList/roomList.csv'

    def readFile(self):

        with open(self.getRoomFilePath()) as roomListFile:
            roomList = csv.reader(roomListFile, delimiter=',')

            for row in roomList:
                self.buildCodes.append(row[0])
                self.roomNum.append(row[1].lstrip('0'))
                self.roomType.append(row[2])
                self.roomFloor.append(row[1].lstrip('0')[0])

    def buildingHTML(self, code, buildingName):

        floordict = {}

        for floornumber in self.roomFloor:
            if floornumber not in floordict:
                key = floornumber
                val = 'Floor'

                floordict[key] = val

        Floor1 = 'Floor 1:;'
        Floor2 = 'Floor 2:;'
        Floor3 = 'Floor 3:;'
        Floor4 = 'Floor 4:;'
        Floor5 = 'Floor 5:;'
        OtherFloor = 'Other:;'

        for i, build in enumerate(self.buildCodes):
            if build == code and self.roomFloor[i] == '1':
                Floor1 += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + \
                          self.roomType[i] + ';'
            elif build == code and self.roomFloor[i] == '2':
                Floor2 += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + self.roomType[
                    i] + ';'
            elif build == code and self.roomFloor[i] == '3':
                Floor3 += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + self.roomType[
                    i] + ';'
            elif build == code and self.roomFloor[i] == '4':
                Floor4 += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + self.roomType[
                    i] + ';'
            elif build == code and self.roomFloor[i] == '5':
                Floor5 += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + self.roomType[
                    i] + ';'
            elif build == code:
                OtherFloor += 'Room Number: ' + self.roomNum[i] + ';' + 'Type: ' + self.roomType[
                    i] + ';'

        if (Floor1 == "Floor 1:;"):
            Floor1 = ""
        if (Floor2 == "Floor 2:;"):
            Floor2 = ""
        if (Floor3 == "Floor 3:;"):
            Floor3 = ""
        if (Floor4 == "Floor 4:;"):
            Floor4 = ""
        if (Floor5 == "Floor 5:;"):
            Floor5 = ""
        if (OtherFloor == "Other:;"):
            OtherFloor = ""

        html = """
                          <h1>""" + buildingName + """</h1><br>

                          <p id="f1">""" + Floor1 + "</p><p id='f2'>" + Floor2 + "</p><p id='f3'>" + Floor3 + "</p><p id='f4'>" + Floor4 + \
               "</p><p id='f5'>" + Floor5 + "</p><p id='fo'>" + OtherFloor + "</p>" + """
                          """
        with open(self.mapfilepath_ + '\\roomList/' + code + '.html', 'w') as fw:
            fw.write(html)
            print('HTML file for ' + buildingName + ' created')

    def createMap(self):
        # UT lat, lon
        UTTCoords = (32.315950, -95.252574)

        # Create map object
        UTmap = folium.Map(location=[32.316137, -95.250997], zoom_start=17, tiles="OpenStreetMap", min_zoom=16,
                           min_lat=32.309790,
                           max_lat=32.32124, min_lon=-95.239071, max_lon=-95.260618, max_bounds=True, zoom_control=True)

        # UTmap.get_root().html.add_child(folium.Element(self.script_str))

        # #Float UT Tyler logo
        #
        # imagefile = 'mapfile/img/UTsquarelogo.PNG'
        # FloatImage(imagefile,).add_to(UTmap)
        #

        # #Event Dummy Point
        # dt = ''
        # for div in self.eventdivs:
        #     dt += '$' + str(div)
        #
        # divtxt = folium.Html(dt, script=True)
        # divWindow = folium.Popup(divtxt, max_width=0)
        # folium.CircleMarker(location=[32.321563,-95.258683], tooltip='EventDivs',
        #                           radius=10, color='black', weight=0, fill_color='Green', fill_opacity=0.2, fill=False,
        #                           popup=divWindow).add_to(UTmap)

        # You are here
        hereTxt = folium.Html('You are here!', script=True)
        hereWindow = folium.Popup(hereTxt, max_width=300)
        hereIcon = folium.Icon(color='red', icon='info-sign')
        folium.Marker(location=UTTCoords, popup=hereWindow, icon=hereIcon).add_to(UTmap)

        # folium.LayerControl().add_to(UTmap)
        # If we add other layers we can turn this back on

        # Adding buildings

        # Fine Arts Complex
        self.buildingHTML('ARC', 'Fine Arts Complex')

        ARChtml = ''

        with open(self.mapfilepath_ + '/roomList/ARC.html', 'r') as CBH:
            for line in CBH:
                ARChtml += line

        arcTxt = folium.Html(ARChtml, script=True)

        arcWindow = folium.Popup(html=arcTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        ARC = folium.CircleMarker(location=[32.315254, -95.258043], tooltip='Fine Arts Complex',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=arcWindow)
        ARC.add_to(UTmap)

        # Biology, Education and Psychology Building
        self.buildingHTML('BEP', 'Biology, Education, Psychology')

        BEPhtml = ''

        with open(self.mapfilepath_ + '/roomList/BEP.html', 'r') as CBH:
            for line in CBH:
                BEPhtml += line

        bepTxt = folium.Html(BEPhtml, script=True)

        bepWindow = folium.Popup(html=bepTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        BEP = folium.CircleMarker(location=[32.317267, -95.252032], tooltip='Biology, Education, Psychology',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=bepWindow)
        BEP.add_to(UTmap)

        # Braithwaite Business Admin Building
        self.buildingHTML('BRB', 'Braithwaite Business Administration')

        BRBhtml = ''

        with open(self.mapfilepath_ + '/roomList/BRB.html', 'r') as CBH:
            for line in CBH:
                BRBhtml += line

        brbTxt = folium.Html(BRBhtml, script=True)

        brbWindow = folium.Popup(html=brbTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        BRB = folium.CircleMarker(location=[32.317341, -95.251512], tooltip='Braithwaite Business Administration',
                                  radius=10, color='black', weight=1, fill_color='Green', fill_opacity=0.2, fill=True,
                                  popup=brbWindow)
        BRB.add_to(UTmap)

        # College of Arts & Sciences
        self.buildingHTML('CAS', 'College of Arts & Sciences')

        CAShtml = ''

        with open(self.mapfilepath_ + '/roomList/CAS.html', 'r') as CBH:
            for line in CBH:
                CAShtml += line

        casTxt = folium.Html(CAShtml, script=True)

        casWindow = folium.Popup(html=casTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        CAS = folium.CircleMarker(location=[32.317285, -95.254262], tooltip='College of Arts & Science',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=casWindow)
        CAS.add_to(UTmap)

        # Soules College of Business
        self.buildingHTML('COB', 'Soules College of Business')

        COBhtml = ''

        with open(self.mapfilepath_ + '/roomList/COB.html', 'r') as CBH:
            for line in CBH:
                COBhtml += line

        cobTxt = folium.Html(COBhtml, script=True)

        cobWindow = folium.Popup(html=cobTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        COB = folium.CircleMarker(location=[32.313234, -95.251733], tooltip='Soules College of Business and Technology',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=cobWindow)
        COB.add_to(UTmap)

        # Cowan Fine and Performing Arts Center
        self.buildingHTML('FAC', 'R. Don Cowan Fine and Performing Arts Center')

        FAChtml = ''

        with open(self.mapfilepath_ + '/roomList/FAC.html', 'r') as CBH:
            for line in CBH:
                FAChtml += line

        facTxt = folium.Html(FAChtml, script=True)

        facWindow = folium.Popup(html=facTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        FAC = folium.CircleMarker(location=[32.318527, -95.251473],
                                  tooltip='R. Don Cowan Fine and Performing Arts Center',
                                  radius=10, color='black', weight=1, fill_color='Orange', fill_opacity=0.2, fill=True,
                                  popup=facWindow)
        FAC.add_to(UTmap)

        # Herrington Patriot Center
        self.buildingHTML('HPC', 'Herrington Patriot Center')

        HPChtml = ''

        with open(self.mapfilepath_ + '/roomList/HPC.html', 'r') as CBH:
            for line in CBH:
                HPChtml += line

        hpcTxt = folium.Html(HPChtml, script=True)

        hpcWindow = folium.Popup(html=hpcTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        HPC = folium.CircleMarker(location=[32.314886, -95.249144],
                                  tooltip='Louise Herrington Patriot Center',
                                  radius=10, color='black', weight=1, fill_color='Orange', fill_opacity=0.2, fill=True,
                                  popup=hpcWindow)
        HPC.add_to(UTmap)

        # Hudnall-Pirtle-Roosth Building
        self.buildingHTML('HPR', 'Hudnall-Pirtle-Roosth Building')

        HPRhtml = ''

        with open(self.mapfilepath_ + '/roomList/HPR.html', 'r') as CBH:
            for line in CBH:
                HPRhtml += line

        hprTxt = folium.Html(HPRhtml, script=True)

        hprWindow = folium.Popup(html=hprTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        HPR = folium.CircleMarker(location=[32.316435, -95.252284],
                                  tooltip='Hudnall-Pirtle-Roosth Building',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=hprWindow)
        HPR.add_to(UTmap)

        # Ingenuity Center
        self.buildingHTML('ICB', 'Ingenuity Center')

        ICBhtml = ''

        with open(self.mapfilepath_ + '/roomList/ICB.html', 'r') as CBH:
            for line in CBH:
                ICBhtml += line

        icbTxt = folium.Html(ICBhtml, script=True)

        icbWindow = folium.Popup(html=icbTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        ICB = folium.CircleMarker(location=[32.311684, -95.241491],
                                  tooltip='Ingenuity Center',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=icbWindow)
        ICB.add_to(UTmap)

        # Robert R. Muntz Library
        self.buildingHTML('LIB', 'Robert R. Muntz Library')

        LIBhtml = ''

        with open(self.mapfilepath_ + '/roomList/LIB.html', 'r') as CBH:
            for line in CBH:
                LIBhtml += line

        libTxt = folium.Html(LIBhtml, script=True)

        libWindow = folium.Popup(html=libTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        LIB = folium.CircleMarker(location=[32.315711, -95.254307],
                                  tooltip='Robert R. Muntz Library',
                                  radius=10, color='black', weight=1, fill_color='Orange', fill_opacity=0.2, fill=False,
                                  popup=libWindow)
        LIB.add_to(UTmap)

        # Ornelas Residence Hall
        self.buildingHTML('ORH', 'Ornelas Residence Hall')

        ORHhtml = ''

        with open(self.mapfilepath_ + '/roomList/ORH.html', 'r') as CBH:
            for line in CBH:
                ORHhtml += line

        OrnelasTxt = folium.Html(ORHhtml, script=True)

        OrnelasWindow = folium.Popup(html=OrnelasTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        ORH = folium.CircleMarker(location=[32.314358, -95.251427], tooltip='Ornelas Residence Hall',
                                  radius=10, color='black', weight=1, fill_color='Red', fill_opacity=0.2, fill=True,
                                  popup=OrnelasWindow)
        ORH.add_to(UTmap)

        # Physical and Health Education Building
        self.buildingHTML('PHE', 'Physical and Health Education Building')

        PHEhtml = ''

        with open(self.mapfilepath_ + '/roomList/PHE.html', 'r') as CBH:
            for line in CBH:
                PHEhtml += line

        pheTxt = folium.Html(PHEhtml, script=True)

        pheWindow = folium.Popup(html=pheTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        PHE = folium.CircleMarker(location=[32.314759, -95.250644], tooltip='Physical and Health Education Building',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=pheWindow)
        PHE.add_to(UTmap)

        # Ratliff Building North
        self.buildingHTML('RBN', 'Ratliff Building North')

        RBNhtml = ''

        with open(self.mapfilepath_ + '/roomList/RBN.html', 'r') as CBH:
            for line in CBH:
                RBNhtml += line

        rbnTxt = folium.Html(RBNhtml, script=True)

        rbnWindow = folium.Popup(html=rbnTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        RBN = folium.CircleMarker(location=[32.317947, -95.253157], tooltip='Ratliff Building North',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=rbnWindow)
        RBN.add_to(UTmap)

        # Ratliff Building South
        self.buildingHTML('RBS', 'Ratliff Building South')

        RBShtml = ''

        with open(self.mapfilepath_ + '/roomList/RBS.html', 'r') as CBH:
            for line in CBH:
                RBShtml += line

        rbnTxt = folium.Html(RBShtml, script=True)

        rbnWindow = folium.Popup(html=rbnTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        RBS = folium.CircleMarker(location=[32.317566, -95.253007], tooltip='Ratliff Building South',
                                  radius=10, color='black', weight=1, fill_color='Blue', fill_opacity=0.2, fill=True,
                                  popup=rbnWindow)
        RBS.add_to(UTmap)

        # James H. Stewart Administration Building
        self.buildingHTML('STE', 'James H. Stewart Administration Building')

        STEhtml = ''

        with open(self.mapfilepath_ + '/roomList/STE.html', 'r') as CBH:
            for line in CBH:
                STEhtml += line

        steTxt = folium.Html(STEhtml, script=True)

        steWindow = folium.Popup(html=steTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        STE = folium.CircleMarker(location=[32.315608, -95.251765], tooltip='James H. Stewart Administration Building',
                                  radius=10, color='black', weight=1, fill_color='Green', fill_opacity=0.2, fill=True,
                                  popup=steWindow)
        STE.add_to(UTmap)

        # University Center
        self.buildingHTML('UC', 'University Center')

        UChtml = ''

        with open(self.mapfilepath_ + '/roomList/UC.html', 'r') as CBH:
            for line in CBH:
                UChtml += line

        ucTxt = folium.Html(UChtml, script=True)

        ucWindow = folium.Popup(html=ucTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        UC = folium.CircleMarker(location=[32.315390, -95.250971], tooltip='University Center',
                                 radius=10, color='black', weight=1, fill_color='Orange', fill_opacity=0.2, fill=True,
                                 popup=ucWindow)
        UC.add_to(UTmap)

        # W.T. Brookshire Hall
        self.buildingHTML('WTB', 'W.T. Brookshire Hall')

        WTBhtml = ''

        with open(self.mapfilepath_ + '/roomList/WTB.html', 'r') as CBH:
            for line in CBH:
                WTBhtml += line

        wtbTxt = folium.Html(WTBhtml, script=True)

        wtbWindow = folium.Popup(html=wtbTxt, max_width=400, min_width=150, parse_html=True)

        # Clickable marker
        WTB = folium.CircleMarker(location=[32.314946, -95.254221], tooltip='W.T. Brookshire Hall',
                                  radius=10, color='black', weight=1, fill_color='Red', fill_opacity=0.2, fill=True,
                                  popup=wtbWindow)
        WTB.add_to(UTmap)

        UTmap.save(self.getMapPath())
        print('HTML file created at ' + self.getMapPath())


if __name__ == '__main__':
    map = MapConstructor()
    map.readFile()
    # map.eventScraper()
    map.createMap()
    map.scriptEvent()
