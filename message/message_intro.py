# 主畫面中的「介紹與說明」進去後的畫面
introduction_message = {
    "type": "bubble",
    "size": "giga",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "功能介紹",
                "weight": "bold",
                "size": "lg",
                "margin": "lg",
                "align": "center"
            },
            {
                "type": "text",
                "text": "🔥 即時查詢股價的簡易小幫手",
                "wrap": True
            },
            {
                "type": "text",
                "text": "🔥　從 Yahoo Finance 即時爬取股價資訊",
                "wrap": True
            },
            {
                "type": "text",
                "text": "🔥　查詢歷史股價收盤震盪圖",
                "wrap": True
            },
{
                "type": "text",
                "text": "🔥　顯示本作業所使用的 FSM 圖",
                "wrap": True
            },
            {
                "type": "text",
                "text": "使用說明",
                "weight": "bold",
                "size": "lg",
                "margin": "lg",
                "align": "center"
            },
            {
                "type": "text",
                "text": "💡　輸入「主選單」或點擊快捷鍵開始操作",
                "wrap": True
            },
            {
                "type": "text",
                "text": "💡　主選單請拖曳後橫向(左右)滑動",
                "wrap": True
            },
            {
                "type": "text",
                "text": "題外話",
                "weight": "bold",
                "size": "lg",
                "margin": "lg",
                "align": "center"
            },
            {
                "type": "text",
                "text": "這是小弟一個簡易的爬取股價作品，歡迎指教 😎",
                "wrap": True
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
