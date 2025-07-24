from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


#line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
#line_handler = WebhookHandler('LINE_CHANNEL_SECRET')

line_bot_api = LineBotApi('8uYnUXVel0cqNllw+ORRj0q16HepXCUmc3+zpMTqPxyMnU8csqgf0Lft+35XU8mL6fLsmIYUVyL/kVyExJLL2/3KjGqQ+vt4rd440e/cf51k11nmjKeGrYuHbLobyRx53Z5Va0t9RikDriQIVXnlnQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('17c2914e2381b70e4c697614728db454')


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api.push_message('U9e67004c725cb0094e823a1bfab53524', TextSendMessage(text='Hello World!!!'))