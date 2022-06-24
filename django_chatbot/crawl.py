import requests
from bs4 import BeautifulSoup
import random

class Food:
    def __init__(self, area):
        self.area = area

    def scrape(self):
        url= "https://ifoodie.tw/explore/" + self.area + "/list?opening=true"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards =  soup.find＿all(
            "div", {"class": "jsx-3292609844 restaurant-info"})

        ans = []
        for card in cards:
            ans.append(card.text)
        index = random.randint(0, len(ans))
        # cards =  soup.find_all(
        #     'div', {'class': 'jsx-1776651079 restaurant-info'}, limit=5)
        # content = ""
        # for card in cards:
 
        #     title = card.find(  # 餐廳名稱
        #         "a", {"class": "jsx-1776651079 title-text"}).getText()
 
        #     stars = card.find(  # 餐廳評價
        #         "div", {"class": "jsx-1207467136 text"}).getText()
 
        #     address = card.find(  # 餐廳地址
        #         "div", {"class": "jsx-1776651079 address-row"}).getText()
 
 
        #     #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
        #     content += f"{title} \n{stars}顆星 \n{address} \n\n"
 
        return ans[index]