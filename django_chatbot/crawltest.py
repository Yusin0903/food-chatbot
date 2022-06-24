import sys
sys.path.append("/Users/zyusin/side_project/lineChatbot/django_chatbot")
import crawl
a = crawl.Food("台南市")
print(a.scrape())