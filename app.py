#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.oli import *
from events.Msg_Template import *
from model.mongodb import *
from events.EXRate import *
import re
import datetime
import twstock

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
    profile = line_bot_api.get_profile(event.source.user_id) #抓取使用者個人資訊
    uid = profile.user_id

    message_text = str(event.message.text).lower()#抓取使用者所傳送的訊息 並改成字串和小寫方便工程師處理
    msg = str(event.message.text).upper().strip()
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱
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
#股票查詢
    if re.match("想知道股價[0-9]", msg):
        stockNumber = msg[5:9]
        btn_msg = stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0

#新增使用者關注的股票到mongodb
    if re.match("關注[0-9]{4}[<>][0-9]",msg):#使用者新增股票至股票清單    
        stockNumber = msg[2:6]
        line_bot_api.push_message(uid, TextSendMessage('加入股票代號'+stockNumber))
        content = write_my_stock(uid, user_name,stockNumber,msg[6:7],msg[7:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    # else:
    #     content = write_my_stock(uid, user_name, stockNumber, "未設定",'未設定')
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if (emsg.startswith('#')):
        text = emsg[1:]
        content =''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content +='%s (%s) %s\n' % (
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content += '最高: %s / 最低:%s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        
        content += '量: %s\n'%(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text=content)
        )
###################匯率區#############################
    if re.match('幣別種類', emsg):
        message = show_Button()
        line_bot_api.reply_message(event.reply_token,message)
    
    if re.match('換匯[A-Z]{3}/[A-Z{3}]',msg):
        line_bot_api.push_message(uid,TextSendMessage('將為您做外匯計算...'))
        content = getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))


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

