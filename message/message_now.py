# 1203 不能用，不知道為甚麼?
# 可能是因為 "type": "carousel" 不能只有一個項目?
# value_now = {
#   "type": "carousel",
#   "contents": [
#     {
#       "type": "bubble",
#       "size": "giga",
#       "hero": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "text",
#             "text": "台積電即時股價",
#             "align": "start",
#             "margin": "md",
#             "size": "xxl",
#             "weight": "bold",
#             "wrap": True
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "$498.50",
#                 "align": "center",
#                 "margin": "md",
#                 "size": "4xl",
#                 "weight": "regular"
#               }
#             ]
#           }
#         ]
#       },
#       "footer": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "查詢股價詳細資訊",
#               "text": "查詢股價詳細資訊"
#             },
#             "height": "md",
#             "color": "#00cc66",
#             "style": "primary"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "結束本次操作",
#               "text": "結束本次操作"
#             },
#             "height": "md",
#             "color": "#00cc66",
#             "style": "primary"
#           }
#         ],
#         "spacing": "lg"
#       }
#     }
#   ]
# }

value_now = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "台積電即時股價",
                "weight": "bold",
                "size": "xl",
                "margin": "md"
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "最新收盤價",
                                "size": "md",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$498.50",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "button",
                "style": "primary",
                "action": {
                    "type": "message",
                    "label": "查詢股價詳細資訊",
                    "text": "詳細股價"
                },
                "height": "md",
                "offsetBottom": "md"
            },
            {
                "type": "button",
                "style": "primary",
                "action": {
                    "type": "message",
                    "label": "結束本次操作",
                    "text": "主選單"
                },
                "height": "md",
                "offsetTop": "none"
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
