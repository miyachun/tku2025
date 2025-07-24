from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
app = Flask(__name__)

#line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
#line_handler = WebhookHandler('LINE_CHANNEL_SECRET')

line_bot_api = LineBotApi('8uYnUXVel0cqNllw+ORRj0q16HepXCUmc3+zpMTqPxyMnU8csqgf0Lft+35XU8mL6fLsmIYUVyL/kVyExJLL2/3KjGqQ+vt4rd440e/cf51k11nmjKeGrYuHbLobyRx53Z5Va0t9RikDriQIVXnlnQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('17c2914e2381b70e4c697614728db454')

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        
  
    if getA=='0':
        UserId = event.source.user_id        
        profile = line_bot_api.get_profile(UserId)
        print(profile)        
        #profile.display_name
        #profile.user_id
        #profile.picture_url
        #profile.status_message
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text=profile.display_name), TextSendMessage(text=profile.user_id)])
        #line_bot_api.reply_message(event.reply_token,TextSendMessage([{type:"text","text":"aa"},{type:"text","text":"bb"}])))              
    
    
    
    
    else:   
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))

if __name__ == "__main__":
    app.run()