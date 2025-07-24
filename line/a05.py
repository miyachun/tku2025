from flask import Flask, request


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

import json
app = Flask(__name__)



@app.route("/")
def home():
  line_bot_api = LineBotApi('8uYnUXVel0cqNllw+ORRj0q16HepXCUmc3+zpMTqPxyMnU8csqgf0Lft+35XU8mL6fLsmIYUVyL/kVyExJLL2/3KjGqQ+vt4rd440e/cf51k11nmjKeGrYuHbLobyRx53Z5Va0t9RikDriQIVXnlnQdB04t89/1O/w1cDnyilFU=')
  try:
    line_bot_api.push_message('U9e67004c725cb0094e823a1bfab53524', TextSendMessage(text='Hello World99999!!!'))
    return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    app.run()