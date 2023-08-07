from line_bot_api import *


def about_us_event(event):
    
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
    
    text_message = TextSendMessage(text = '''$ Tyler $ 
Hello~ 歡迎您的加入~
成為Tyler的好友!
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
    
def push_msg(eveent,msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id,TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id,TextSendMessage(text=msg))


def Usage(event):
    push_msg(event,"⭐⭐ 查尋方法 ⭐⭐\
             \n\
             \n👉小幫手可以查詢油價 \
             \n\
             \n👉油價通知\
             \n👉匯率\
             \n👉使用說明\
             \n👉自動提醒\
             \n👉趨勢分析")