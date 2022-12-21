# -*- coding: utf-8 -*-
'''
即時股價
'''
import datetime

# https://stackoverflow.com/questions/49921721/runtimeerror-main-thread-is-not-in-main-loop-with-matplotlib-and-flask
import matplotlib
import pandas as pd
import requests

# 坑
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas_datareader as pdr
from bs4 import BeautifulSoup
import pyimgur
from matplotlib.font_manager import FontProperties  # 設定字體

import yfinance as yf
yf.pdr_override()

font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

# pyimgur
CLIENT_ID = "YOUR_CLIENT_ID"

def get_stock_name(stockNumber):
    try:
        url = f'https://tw.stock.yahoo.com/q/q?s={stockNumber}'
        re = requests.get(url)
        soup = BeautifulSoup(re.text, 'html.parser')
        title = soup.find('title')
        stock_name = title.text.split('(')[0]
        return stock_name
    except:
        return "Unavailable"


# 使用者查詢股票
def getprice(stockNumber):
    stock_name = get_stock_name(stockNumber)
    if stock_name == "Unavailable": return "股票代碼錯誤!"

    stock = yf.download(f'{stockNumber}.TW', end=datetime.datetime.now())
    date = stock.index[-1]
    price = '%.2f ' % stock["Close"][-1]  # 近日之收盤價
    last_price = '%.2f ' % stock["Close"][-2]  # 前一日之收盤價
    spread_price = '%.2f ' % (float(price) - float(last_price))  # 價差
    spread_ratio = '%.2f ' % (float(spread_price) / float(last_price))  # 漲跌幅
    spread_price = spread_price.replace("-", '▽ ') if last_price > price else '△ ' + spread_price
    spread_ratio = spread_ratio.replace("-", '▽ ') if last_price > price else '△ ' + spread_ratio
    open_price = str('%.2f ' % stock["Open"][-1])  # 近日之開盤價
    high_price = str('%.2f ' % stock["High"][-1])  # 近日之盤中高點
    low_price = str('%.2f ' % stock["Low"][-1])  # 近日之盤中低點
    price_five = stock.tail(5)["Close"]  # 近五日之收盤價
    stockAverage = str('%.2f ' % pd.to_numeric(price_five).mean())  # 計算近五日平均價格
    stockSTD = str('%.2f ' % pd.to_numeric(price_five).std())  # 計算近五日標準差
    info = [date, price, open_price, high_price, low_price, spread_price, spread_ratio, stockAverage, stockSTD]

    return info


# 畫股價震盪圖
# 此函式需要 msjh.ttf 字體檔案
def show_fluctuation(stockNumber):
    stock_name = get_stock_name(stockNumber)
    end = datetime.datetime.now()
    date = end.strftime("%Y%m%d")
    year = str(int(date[0:4]) - 1)
    month = date[4:6]
    stock = yf.download(f'{stockNumber}.TW', end=end)

    stock['stock_fluctuation'] = stock["High"] - stock["Low"]
    max_value = max(stock['stock_fluctuation'][:])  # 最大價差
    min_value = min(stock['stock_fluctuation'][:])  # 最小價差
    plt.figure(figsize=(12, 6))
    plt.plot(stock['stock_fluctuation'], '-', label="波動度", color="orange")
    plt.title(f"{stock_name} 收盤價震盪圖", loc='center', fontsize=20, fontproperties=font_path)  # loc->title 的位置
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.ylabel('價格', fontsize=20, fontproperties=font_path)
    plt.grid(True, axis='y')  # 網格線
    plt.legend(fontsize=14, prop=font_path)
    plt.savefig(f'{stockNumber}_fluctuation.png')  # 存檔
    # plt.show()
    plt.close()
    # upload to imgur and get url
    PATH = f"{stockNumber}_fluctuation.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="upload")
    return uploaded_image.link

# print(getprice(2330))
# print(show_fluctuation(2330))