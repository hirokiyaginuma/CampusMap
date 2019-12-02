import os, re, requests, shutil
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image


class Event():
    def __init__(self):
        self.eventName = list()
        self.eventDate = list()
        self.eventLocation = list()
        self.imageURL = list()
        self.url = "https://uttyler.campuslabs.com/engage/events"
        self.eventListPath_ = os.getcwd() + '\\mapfile\\event\\'
        self.imageLocation_ = os.getcwd() + '\\mapfile\\eventimage\\'
        self.geckodriverPath_ = os.getcwd() + '\\mapfile\\geckodriver-v0.26.0-win64\\geckodriver.exe'

    def getEvent(self):
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Firefox(executable_path=self.geckodriverPath_, options=options)
        driver.get(self.url)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, 'lxml')

        event = soup.find('div', id='event-discovery-list')

        events = event.find_all('a')

        for x in events:
            self.eventName.append(str(x.h3.text))
            a = x.div.div.find('div', {"style" : "padding: 0px 0px 46px; position: relative; height: 100%;"})
            self.eventDate.append(a.div.div.text)
            self.eventLocation.append(a.div.find('div', {"style" : "white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"}).text)

            y = x.div.div.div.div.div.div
            z = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(y))
            if z:
                self.imageURL.append(z[0])
            else:
                self.imageURL.append(None)

        with open(self.eventListPath_ + 'name.txt', 'w') as fw:
            fw.writelines("%s\n" % place for place in self.eventName)
        with open(self.eventListPath_ + 'date.txt', 'w') as fw:
            fw.writelines("%s\n" % place for place in self.eventDate)
        with open(self.eventListPath_ + 'location.txt', 'w') as fw:
            fw.writelines("%s\n" % place for place in self.eventLocation)

    def readList(self):
        with open(self.eventListPath_ + 'name.txt', 'r') as fw:
            filecontents = fw.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.eventName.append(current_place)
        with open(self.eventListPath_ + 'date.txt', 'r') as fw:
            filecontents = fw.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.eventDate.append(current_place)
        with open(self.eventListPath_ + 'location.txt', 'r') as fw:
            filecontents = fw.readlines()
            for line in filecontents:
                current_place = line[:-1]
                self.eventLocation.append(current_place)

    def downloadImage(self):
        self.deleteImage()

        for i in range(len(self.imageURL)):
            if self.imageURL[i]:
                resp = requests.get(self.imageURL[i], stream=True)
                image_file = open(self.imageLocation_ + str(i) + '.png', 'wb')
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, image_file)
                del resp

        self.convertToJpg()

    def deleteImage(self):
        for root, dirs, files in os.walk(self.imageLocation_):
            for file in files:
                os.remove(os.path.join(root, file))

    def convertToJpg(self):
        for i in range(len(self.imageURL)):
            try:
                im = Image.open(self.imageLocation_ + str(i) + ".png")
                rgb_im = im.convert('RGB')
                rgb_im.save(self.imageLocation_ + str(i) + '.jpg')
                im.close()

                basewidth = 300
                img = Image.open(self.imageLocation_ + str(i) + '.jpg')
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img.save(self.imageLocation_ + str(i) + '.jpg')
                img.close()
            except IOError:
                continue

    def printList(self):
        for i in range(len(self.eventName)):
            print(self.eventName[i])
            print(self.eventDate[i])
            print(self.eventLocation[i])
            print(self.imageURL[i])
            print()

if __name__ == '__main__':
    event = Event()
