#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)
#必須放上自己的Channel Access Token
line_bot_api =LineBotApi('CcPIRDmSCr2g3LpNQIg9lciiw4XcfcVegmkhexA2G7M3YAug9IeouBbmNiKGsyHpT1u9PirnVwuE6ntv4URHFU9MS/H//9b1LUcaVFUJwBUMhdPeAygnO9t5D0mI46MhCwZr2S4HAh1v3lmD2a2TvgdB04t89/1O/w1cDnyilFU=')
# 必須要放上自己的Channel Secret
handler = WebhookHandler('e0bd788d0809c2df251e29c9514ac05c')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-LineSignature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    #handel webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

#處理訊息(回傳同樣的訊息)
@handler.add(MessageEvent, message=TextMessage)
def handel_message(event):
  
    emoji = [
            {
                "index":0,
                "productId": "5ac21c46040ab15980c9b442",
                "emojiId": "020"
            },
                        {
                "index":8,
                "productId": "5ac21c46040ab15980c9b442",
                "emojiId": "020"
            }
        ]
    
    text_message = TextSendMessage(text = '''$ Tyler $ Hello~ 歡迎您的加入~成為Tyler的好友!
    我是Tyler 您的小幫手
    這裡有許多的股票資訊
   可以直接點選下面的功能來使用~''', emojis = emoji)
  
  
   # message = TextSendMessage(text = event.message.text)
    #line_bot_api.reply_message(event.reply_token,message)

    Sticker_message = StickerSendMessage(
        package_id = '11539',
        sticker_id='52114118'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, Sticker_message])
if __name__ == '__main__':
    app.run()