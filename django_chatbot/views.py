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
import random
import requests
from bs4 import BeautifulSoup
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        try:
            events = parse_line_request(request)
        except (InvalidSignatureError, LineBotApiError):
            return HttpResponseForbidden()

        handle_line_events(events)
        return HttpResponse()

    return HttpResponseBadRequest()

def parse_line_request(request):
    signature = request.META.get('HTTP_X_LINE_SIGNATURE', '')
    body = request.body.decode('utf-8')
    return parser.parse(body, signature)

def handle_line_events(events):
    city = ["台北市", "新北市", "桃園市", "新竹市", "新竹縣", "苗栗縣", "台中市", "南投縣", "雲林縣", "雲林市", "嘉義縣", "嘉義市", "台南市", "高雄市", "屏東縣",
            "屏東市", "花蓮縣", "台東縣", "宜蘭縣", "蘭嶼", "綠島"]
    eastriver = ["幸福食堂", "都蘭小房子", "貴煮良食", "小鐵匠廚房", "舊街東河包子", "東河包子", "洛恩米薩克", "興文小吃", "哇哇哇大骨麵", "源發餐廳"]

    for event in events:
        if isinstance(event, MessageEvent):
            handle_message_event(event, city, eastriver)

def handle_message_event(event, city, eastriver):
    if "冰冰" in event.message.text:
        reply_text = "您好我是冰冰，請輸入您要選擇吃飯的城市以及地區。例如：台南市,台南市北區，冰冰將會幫你挑選目前有營業的餐廳！！如要尋找最新餐廳或人氣餐廳，請依照此方式。例如：台南市北區-人氣 台北市信義區-最新。"
        line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))
    elif "台東縣東河鄉" in event.message.text:
        idx = random.randint(0, len(eastriver))
        line_bot_api.reply_message(event.reply_token, TextMessage(text=eastriver[idx]))
    else:
        handle_city_search(event, city)

def handle_city_search(event, city):
    for i in city:
        if i in event.message.text:
            handle_city_search_details(event, i)

def handle_city_search_details(event, city):
    info_parts = event.message.text.split("-")
    if len(info_parts) < 2:
        city_name = city
        area = event.message.text.lstrip(city_name)
        category = ""
    else:
        if info_parts[1] == "人氣":
            city_name = city
            area = info_parts[0].lstrip(city_name)
            category = "&sortby=rating"
        elif info_parts[1] == "最新":
            city_name = city
            area = info_parts[0].lstrip(city_name)
            category = "&sortby=recent"

    reply_text = scrapecity(city_name, area, category)
    line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))

def scrapecity(city, area, category):
    if city and area:
        url = f"https://ifoodie.tw/explore/{city}/{area}/list?opening=true{category}"
    elif city:
        url = f"https://ifoodie.tw/explore/{city}/list?opening=true{category}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", {"class": "jsx-3292609844 restaurant-info"})

    ans = [card.text for card in cards]
    index = random.randint(0, len(ans) - 1) if ans else 0
    return ans[index] if ans else "No results found"
