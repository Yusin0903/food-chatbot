import requests
import random
from bs4 import BeautifulSoup
def scrapearea(area):
    url= "https://ifoodie.tw/explore/list?opening=true&poi=" + area
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards =  soup.find＿all(
            "div", {"class": "jsx-3292609844 restaurant-info"})

    ans = []
    for card in cards:
        ans.append(card.text)
    return ans
def scrapecity(city, area,category):
        if city and area:
            url= "https://ifoodie.tw/explore/" + city+ "/"+ area + "/list?opening=true"+ category
        elif city:
             url= "https://ifoodie.tw/explore/" + city+ "/list?opening=true"+ category

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards =  soup.find＿all(
            "div", {"class": "jsx-3292609844 restaurant-info"})

        ans = []
        for card in cards:
            ans.append(card.text)
        index = random.randint(0, len(ans))
        return ans[index]
a = "台南市東區-人氣"
b = "台南市"
c = a.split("-")
d = c[0].lstrip(b)
category = "&sortby=recent"
val = scrapecity(b,d,category)
print(val)
if not val :
    print("yes")
