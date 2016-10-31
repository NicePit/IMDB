import requests
from bs4 import BeautifulSoup



class extractor1(object):

    def __init__(self, id):
        self.url = "http://www.imdb.com/search/name?gender=female&start="+str(id)

    def scrape(self):
        rating_list = []
        url_list = []
        rating_page = requests.get(self.url)
        rating_soup = BeautifulSoup(rating_page.content)
        data = rating_soup.find_all("td", {"class": "name"})
        for item in data:
            rating_list.append(str(item).split('"')[3])
        for item in rating_list:
            url_list.append("http://www.imdb.com"+item)
        self.url_list = url_list


class extractor2(object):

    def __init__(self, link):
        self.url = link
        self.scrape()
        self.get_picture()
        # self.get_gender()
        self.down_data()

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

    # def get_gender(self):
    #
    #     data = self.soup.find_all("span",{"class": "itemprop"})
    #     if data:
    #         if "Actor" in str(data):
    #             self.gender = 1
    #         else:
    #             self.gender = 0

    def down_data(self):
        # urllib.urlretrieve(self.pic_url , '/home/stanislav/PycharmProjects/IMDB/pics/' + self.pic_name)
        if self.pic_url is not None:
            with open("Gen_info1.txt", "a") as text_file:
                    text_file.write(self.pic_url + " 0\n")
        else:
            pass

count = 0

for item in range(1,100000,50):
    people = extractor1(item)
    people.scrape()

    for link in people.url_list:
        try:
            person = extractor2(link)
        except Exception as exception:
            print exception

    count += 1
    print count*50










