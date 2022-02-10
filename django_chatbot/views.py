from selectors import EpollSelector
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
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

        for event in events:
            if isinstance(event, MessageEvent):# 如果有訊息事件
                if "冰冰" in event.message.text:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=find_dinner(event.message.text))
                    )
                elif "小小兵" in event.message.text:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage("請叫我小冰冰www")
                    )
                elif "學姊" in event.message.text:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage("不要叫我學姊，叫我冰冰姐www"),
                    )
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        ImageSendMessage(
                            original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                            preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                        )
                    )
                        
                elif "學姐" in event.message.text:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage("不要叫我學姐，叫我冰冰姐"),
                    )
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        ImageSendMessage(
                            original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                            preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                        )
                    )
                elif "阿冰" in event.message.text:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        ImageSendMessage(
                            original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                            preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                        )
                    )
                   



        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def find_dinner(event):
    return "你好我是冰冰www"
    
