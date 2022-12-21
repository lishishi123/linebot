import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage

# 從 .env 檔中取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


# https://github.com/chonyy/daily-nba/blob/master/src/utils.py
def send_image_url(id, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)

    return "OK"


"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""
