import requests
from bs4 import BeautifulSoup
import urllib


class Extractor(object):

    # male = 1
    # female = 0

    def __init__(self, id):
        self.url = "http://www.imdb.com/name/nm"+str(id)
        self.count = id

    def scrape(self):

        profile_page = requests.get(self.url)
        self.soup = BeautifulSoup(profile_page.content)

    def get_picture(self):
        data = self.soup.find_all("img",{"id": "name-poster"})
        if data:
            pic_splitted = str(data).split('"')
            self.pic_url = pic_splitted[9]
            self.pic_name = str(self.pic_url).split("/")[5]
        else:
            self.pic_url = None

    def get_gender(self):

        data = self.soup.find_all("span",{"class": "itemprop"})
        if data:
            if "Actor" in str(data):
                self.gender = 1
            else:
                self.gender = 0

    def down_data(self):
        print self.count
        urllib.urlretrieve(self.pic_url , '/home/stanislav/PycharmProjects/IMDB/pics/' + self.pic_name)
        with open("Gen_info.txt", "a") as text_file:
                if self.gender == 1:
                    text_file.write(self.pic_name + " 1\n")
                    return 1
                else:
                    text_file.write(self.pic_name + " 0\n")
                    return 0


for profile in range(20000, 100000):

    person = Extractor(profile)

    try:
        person.scrape()
        person.get_picture()
        person.get_gender()
        person.down_data()

    except Exception as exception:
            print "Found an exception: " + str(exception)


