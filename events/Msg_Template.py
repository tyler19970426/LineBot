from line_bot_api import *

def stock_two_Button():
 
 Button_message = FlexSendMessage(
  alt_text="選單",
  contents={
            "type": "bubble",
            "hero": {
              "type": "image",
              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
              "size": "full",
              "aspectRatio": "20:13",
              "aspectMode": "cover",
              "action": {
                "type": "uri",
                "uri": "https://linecorp.com"
              }
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "spacing": "md",
              "action": {
                "type": "uri",
                "uri": "https://linecorp.com"
              },
              "contents": [
                {
                  "type": "text",
                  "text": "股票",
                  "size": "xl",
                  "weight": "bold"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "股價查詢",
                        "text": "股價查詢"
                      },
                      "style": "primary"
                    }
                  ]
                },
                {
                  "type": "text",
                  "text": "-----------------------------------------------------------------",
                  "wrap": True,
                  "color": "#aaaaaa",
                  "size": "xxs"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "匯率",
                      "size": "xl",
                      "weight": "bold"
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "幣別種類",
                        "text": "幣別種類"
                      },
                      "style": "primary"
                    }
                  ]
                }
              ]
            }
          }
 )
 return Button_message









def stock_reply_other(stockNumber):
    content_text = '及時股價和K線圖'
    text_message = TextSendMessage(
                                    text = content_text ,
                                    quick_reply = QuickReply(
                                        items=[
                                            QuickReplyButton(
                                                    action=MessageAction(
                                                        label='五日股價查詢',
                                                        text = '#'+stockNumber,
                                                    )
                                            ),
                                            QuickReplyButton(
                                                    action = MessageAction(
                                                         label = 'K線圖',
                                                         text = '@K'+stockNumber       
                                                    )   
                                            ),
                                            ]
                                    ))
    return text_message 

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "幣別種類",
        "weight": "bold",
        "size": "xl",
        "color": "#AA2B1D"
      },
      {
        "type": "image",
        "url": "https://i.imgur.com/M0DK02o.png",
        "position": "relative",
        "aspectMode": "cover",
        "size": "full"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "美金",
              "text": "USD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "日圓",
              "text": "JPY"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "港幣",
              "text": "HKD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "英鎊",
              "text": "GBP"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "澳幣",
              "text": "AUD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "加拿大幣",
              "text": "CAD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞士法郎",
              "text": "CHF"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新加坡",
              "text": "SGD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "南非幣",
              "text": "ZAR"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞典幣",
              "text": "SEK"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "泰幣",
              "text": "THB"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "菲比索",
              "text": "PHP"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "印尼幣",
              "text": "IDR"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "韓元",
              "text": "KRW"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "馬來幣",
              "text": "MYR"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#C8E4B2",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "越南盾",
              "text": "VND"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "人民幣",
              "text": "CNY"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "紐元",
              "text": "NZD"
            },
            "gravity": "center",
            "style": "secondary",
            "color": "#9ED2BE",
            "margin": "sm"
          }
        ]
      }
    ]
  }
}
    )
    return flex_message   
