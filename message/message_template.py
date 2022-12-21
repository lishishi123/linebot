# https://developers.line.biz/flex-simulator/
main_menu = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/M9Q6cBL.png",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "1.25:1"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "介紹與說明",
                            "text": "功能介紹與說明"
                        },
                        "height": "md",
                        "color": "#ff9900",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/C8UdDAM.png",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "1.25:1"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "查詢即時股價",
                            "text": "即時股價"
                        },
                        "height": "md",
                        "color": "#ff6666",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/a6azwci.png",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "1.25:1"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "查詢詳細股價資訊",
                            "text": "詳細股價"
                        },
                        "height": "md",
                        "color": "#ff6666",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/SFmXBnt.png",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "1.25:1"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "查詢收盤價震盪圖",
                            "text": "震盪圖"
                        },
                        "height": "md",
                        "color": "#ff66b3",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        },
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/g3ow8sn.png",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "1.25:1"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "FSM",
                            "text": "FSM"
                        },
                        "height": "md",
                        "color": "#008000",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        }
    ]
}

stock_info = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "台積電股價詳細資訊",
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
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "開盤價",
                                "size": "md",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$506.00",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "最高價",
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$508.00",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "最低價",
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$498.50",
                                "size": "md",
                                "color": "#111111",
                                "align": "end",
                                "contents": []
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "價差",
                                "flex": 0,
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "△ 8.50",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "漲跌幅",
                                "flex": 0,
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "△ 0.02",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "近五日平均價格",
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$490.80",
                                "size": "md",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "近五日標準差",
                                "size": "md",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$7.62",
                                "size": "md",
                                "color": "#111111",
                                "align": "end",
                                "contents": []
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
                    "label": "返回主選單",
                    "text": "主選單"
                }
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
