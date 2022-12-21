plot_fluc = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "size": "giga",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/SFmXBnt.png",
                "aspectMode": "fit",
                "size": "full",
                "animated": True,
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "結束本次操作",
                            "text": "主選單"
                        },
                        "height": "md",
                        "color": "#00cc66",
                        "style": "primary"
                    }
                ],
                "spacing": "lg"
            }
        }
    ]
}
