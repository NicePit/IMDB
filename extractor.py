import requests
from bs4 import BeautifulSoup
import urllib


def scrap_imdb(url):

    rating_page = requests.get(url)

    soup = BeautifulSoup(rating_page.content)

    data = soup.find_all("div",{"class": "desc"})

    list_actors = []

    for item in data:
        i=str(item)
        list_actors.append(i.split('"')[3])


    url2 = "http://www.imdb.com"
    count = 0

    for item in list_actors:
        url_profile = url2+item
        try:
            act_profile = requests.get(url_profile)
            soup2 = BeautifulSoup(act_profile.content)
            gender = soup2.find_all("span",{"class": "itemprop"})
            pic = soup2.find_all("div",{"class": "image"})
            pic_splitted = str(pic).split('"')
            picture_name = (pic_splitted[13].split("/"))[5]
            picture_url = pic_splitted[13]
            count += 1
            print count
            urllib.urlretrieve(picture_url , '/home/stanislav/PycharmProjects/IMDB/pics/' + picture_name)



            with open("Gen_info.txt", "a") as text_file:
                if "Actor" in str(gender):
                    text_file.write(picture_name + " 1\n")
                else:
                    text_file.write(picture_name + " 0\n")

            count += 1
            print count
        except Exception as e:
            print e


"""for i in range(0,9):
    url = "http://www.imdb.com/list/ls058011111/?start=" + str(i) +"01&view=grid&sort=listorian:asc"
    scrap_imdb(url)"""



url = "http://www.imdb.com/list/ls058011111/?start=901&view=grid&sort=listorian:asc"
scrap_imdb(url)