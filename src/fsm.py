import os

from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import FlexSendMessage, ImageSendMessage
from transitions.extensions import GraphMachine

# import trick
# from ..message import message_cancel, message_return_menu, message_intro, message_template, message_now, message_show_fsm

from message import message_cancel, message_return_menu, message_intro, message_template, message_now, message_show_fsm


# from message import message_cancel, message_return_menu, message_intro, message_template, message_now, message_show_fsm
from src.stockprice import (
    get_stock_name,
    getprice,
    show_fluctuation
)

load_dotenv()


# is_xxx: 回傳 boolean value，判斷 event.message.text (也就是使用者輸入的內容)
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text == "功能介紹與說明"

    def is_going_to_show_fsm_pic(self, event):
        text = event.message.text
        return text == "FSM"

    def is_going_to_search_value_now(self, event):
        text = event.message.text
        return text == "即時股價"

    def is_going_to_value_now(self, event):
        return True

    def is_going_to_search_value_full(self, event):
        text = event.message.text
        return text == "詳細股價"

    def is_going_to_value_full(self, event):
        return True

    def is_going_to_search_fluctuation(self, event):
        text = event.message.text
        return text == "震盪圖"

    def is_going_to_fluctuation(self, event):
        return True

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_show_fsm_pic(self, event):
        print("I'm entering show_fsm_pic")
        reply_token = event.reply_token

        image_message = ImageSendMessage(
            original_content_url="https://i.imgur.com/MoV4mCC.png",
            preview_image_url="https://i.imgur.com/MoV4mCC.png"
        )
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))

        fsm = message_show_fsm.fsm
        message_to_reply = FlexSendMessage('FSM', fsm)

        line_bot_api.reply_message(reply_token, [image_message, message_to_reply])
        self.go_back()

    def on_enter_cancel(self, event):
        print("I'm entering cancel")
        reply_token = event.reply_token
        message = message_cancel.cancel_menu
        message_to_reply = FlexSendMessage("結束並返回主選單", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_introduction(self, event):
        print("I'm entering introduction")
        reply_token = event.reply_token
        message = message_intro.introduction_message
        message_to_reply = FlexSendMessage("功能介紹與說明", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_value_now(self, event):
        print("I'm entering value_now")
        reply_token = event.reply_token
        stock_number = str(event.message.text)  # 使用者輸入的內容
        print(f"輸入: {stock_number}")
        stock_name = get_stock_name(stock_number)
        print(f"輸入的股價名稱為: {stock_name}")
        info_list = getprice(stock_number)
        print(info_list)
        table = message_now.value_now

        table["body"]["contents"][0]["text"] = f'{stock_name}即時股價'
        table["body"]["contents"][2]["contents"][0]["contents"][1]["text"] = info_list[1]

        print(table)

        message_to_reply = FlexSendMessage("即時股價", table)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_value_full(self, event):
        print("I'm entering value_full")
        reply_token = event.reply_token
        stock_number = str(event.message.text)  # 使用者輸入的內容
        stock_name = get_stock_name(stock_number)
        info_list = getprice(stock_number)
        print(info_list)
        table = message_template.stock_info

        table["body"]["contents"][0]["text"] = f'{stock_name}股價詳細資訊'
        table["body"]["contents"][2]["contents"][0]["contents"][0]["text"] = "最新收盤價"
        table["body"]["contents"][2]["contents"][0]["contents"][1]["text"] = info_list[1]
        table["body"]["contents"][2]["contents"][1]["contents"][0]["text"] = "開盤價"
        table["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = info_list[2]
        table["body"]["contents"][2]["contents"][2]["contents"][0]["text"] = "最高價"
        table["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = info_list[3]
        table["body"]["contents"][2]["contents"][3]["contents"][0]["text"] = "最低價"
        table["body"]["contents"][2]["contents"][3]["contents"][1]["text"] = info_list[4]
        table["body"]["contents"][2]["contents"][4]["contents"][0]["text"] = "價差"
        table["body"]["contents"][2]["contents"][4]["contents"][1]["text"] = info_list[5]
        table["body"]["contents"][2]["contents"][5]["contents"][0]["text"] = "漲跌幅"
        table["body"]["contents"][2]["contents"][5]["contents"][1]["text"] = info_list[6]
        table["body"]["contents"][2]["contents"][6]["contents"][0]["text"] = "近五日平均價格"
        table["body"]["contents"][2]["contents"][6]["contents"][1]["text"] = info_list[7]
        table["body"]["contents"][2]["contents"][7]["contents"][0]["text"] = "近五日標準差"
        table["body"]["contents"][2]["contents"][7]["contents"][1]["text"] = info_list[8]

        message_to_reply = FlexSendMessage(f'{stock_name}股價詳細資訊', table)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_fluctuation(self, event):
        print("I'm entering fluctuation")
        reply_token = event.reply_token
        stock_number = str(event.message.text)  # 使用者輸入的內容
        stock_name = get_stock_name(stock_number)
        furl = show_fluctuation(stock_number)

        image_message = ImageSendMessage(
            original_content_url=furl,
            preview_image_url=furl
        )
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        # line_bot_api.reply_message(reply_token, image_message)

        return_menu = message_return_menu.return_menu
        message_to_reply = FlexSendMessage(f'{stock_name}趨勢圖', return_menu)

        line_bot_api.reply_message(reply_token, [image_message, message_to_reply])

        self.go_back()

# machine.get_graph().draw("fsm.png", prog="dot", format="png")
