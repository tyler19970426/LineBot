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
    except IndentationError:
        abort(400)

    return "OK"

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handel_message(event):
    message = TextSendMessage(text = event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

if __name__ == '__main__':
    app.run()