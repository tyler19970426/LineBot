#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.oli import *
app = Flask(__name__)

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

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handel_message(event):  
    #可以回傳使用者ID
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id

    message_text = str(event.message.text).lower()

#######################使用說明 選單 油價查詢#################   
    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)

    if message_text =='想知道油價':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        ) 

#######################股票區################
if event.message.text =='股價查詢':
    line_bot_api.push_message(uid, TextSendMessage('請輸入#+股票代號....'))

##############封鎖和解封################
@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg ="""Hello~ 歡迎您的加入~
成為Tyler的好友!
我是Tyler 您的小幫手
這裡有許多的股票資訊
可以直接點選下面的功能來使用~"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ == '__main__':
    app.run()

