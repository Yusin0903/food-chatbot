from selectors import EpollSelector
from unicodedata import category
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
import random
import requests
from bs4 import BeautifulSoup
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        city = ["台北市","新北市","桃園市","新竹市","新竹縣","苗栗縣","台中市","南投縣","雲林縣","雲林市","嘉義縣","嘉義市","台南市","高雄市","屏東縣","屏東市","花蓮縣","台東縣","宜蘭縣","蘭嶼","綠島"]
        eastriver =["幸福食堂","都蘭小房子","貴煮良食","小鐵匠廚房","舊街東河包子","東河包子","洛恩米薩克","興文小吃","哇哇哇大骨麵","源發餐廳"]
        for event in events:

            if isinstance(event, MessageEvent):# 如果有訊息事件
                if "冰冰" in event.message.text:
                    # reply_arr =[]
                    # reply_arr.append(AudioSendMessage(original_content_url = "https://dl.dropbox.com/s/6m5mjnybykpevlv/%E5%86%B0%E5%86%B0.mp3?dl=0", duration=2000))
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        # TextSendMessage(text=find_dinner(event.message.text))
                        TextMessage(text = "您好我是冰冰，請輸入您要選擇吃飯的城市以及地區。例如：台南市,台南市北區，冰冰將會幫你挑選目前有營業的餐廳！！如要尋找最新餐廳或人氣餐廳，請依照此方式。例如：台南市北區-人氣 台北市信義區-最新。")
                    )
                for i in city:
                    if i in event.message.text:
                        all = event.message.text.split("-")
                        if len(all)<2:
                            city =i
                            area = event.message.text.lstrip(i)
                            category = ""
                        else:
                            if all[1] == "人氣":
                                city = i
                                area = all[0].lstrip(i)
                                category = "&sortby=rating"
                            elif all[1] == "最新":
                                city = i
                                area = all[0].lstrip(i)
                                category = "&sortby=recent"
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextMessage(text = scrapecity(city, area, category))
                        )
                if "東河" in event.message.text:
                    idx = random.randint(0, len(eastriver))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextMessage(text = eastriver[idx])
                    )

                    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def find_dinner(event):
    return "你好我是冰冰www"

def scrapecity(city, area, category):
        if city and area:
            url= "https://ifoodie.tw/explore/" + city+ "/"+ area + "/list?opening=true" + category
        elif city:
             url= "https://ifoodie.tw/explore/" + city+ "/list?opening=true" + category

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards =  soup.find＿all(
            "div", {"class": "jsx-3292609844 restaurant-info"})

        ans = []
        for card in cards:
            ans.append(card.text)
        index = random.randint(0, len(ans))
        return ans[index]


