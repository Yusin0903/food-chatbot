import sys
sys.path.append("/Users/zyusin/side_project/lineChatbot/django_chatbot")
import crawl
a = crawl.Food("台南市")
print(a.scrape())
# elif "小小兵" in event.message.text:
                #     line_bot_api.reply_message(  # 回復傳入的訊息文字
                #         event.reply_token,
                #         TextSendMessage("請叫我小冰冰www")
                #     )
                # elif "學姊" in event.message.text:
                #     reply_arr =[]
                #     reply_arr.append(TextSendMessage("不要叫我學姊，叫我冰冰姊"))
                #     reply_arr.append(ImageSendMessage(
                #             original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                #             preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                #         ))
                #     line_bot_api.reply_message(  # 回復傳入的訊息文字
                #         event.reply_token,
                #         reply_arr
                #     )
                        
                # elif "學姐" in event.message.text:
                #     reply_arr =[]
                #     reply_arr.append(TextSendMessage("不要叫我學姐，叫我冰冰姐"))
                #     reply_arr.append(ImageSendMessage(
                #             original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                #             preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                #         ))
                #     line_bot_api.reply_message(  # 回復傳入的訊息文字
                #         event.reply_token,
                #         reply_arr
                #     )
                    
                # elif "阿冰" in event.message.text:
                #     line_bot_api.reply_message(  # 回復傳入的訊息文字
                #         event.reply_token,
                #         ImageSendMessage(
                #             original_content_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg",
                #             preview_image_url="https://img.ltn.com.tw/Upload/ent/page/800/2021/02/25/phpXzdxxD.jpg"
                #         )
                #     )
                   
