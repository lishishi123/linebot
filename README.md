# TOC Final Project
## Setup
### Prerequisite
- Python 3.8
- Anaconda or similar virtual environment
- Line
- HTTPS Server

### Install Dependency (Requirement Packages)
```
$ pip install -r requirements.txt
```
- pygraphviz (For visualizing Finite State Machine)
    - [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	- [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


### Secret Data
- You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
- `LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
- Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

### Ngrok installation
- [macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```
$ brew cask install ngrok
```

`ngrok` would be used in the following instruction**

```
$ ngrok http 8000
```

After that, `ngrok` would generate a https URL.

### Run the sever

```sh
$ python -m src.app
```
:notes: NOT `python app.py`
## Finite State Machine
![](https://i.imgur.com/EKe79yr.png)

1. 初始狀態是設定在 `user` state，一旦輸入「主選單」或是點擊相對應的快捷鍵，就走到 `menu` state。
2. 在 `menu` state 中，輸入以下指令或者是點擊畫面中出現的相對應快捷鍵，可以走到指定的功能狀態，例如輸入:
- 「功能介紹與說明」或
- 「即時股價」或
- 「詳細股價」或
- 「震盪圖」或
- 「FSM」

以下進行詳細的功能說明。

# Usage
## QRCode
![](https://i.imgur.com/OSMt6CE.png)

## 主選單
輸入「主選單」，進入主畫面，主畫面中提供本 linebot 五個功能的快捷鍵。

![](https://i.imgur.com/477rvNr.png)

五個功能如下，後面會詳細介紹:

![](https://i.imgur.com/WhgHKfj.png)

## 介紹與說明
點擊「介紹與說明」快捷鍵，或者是輸入「功能介紹與說明」，可以顯示並介紹本 linebot 提供的所有功能，如下面兩張圖:

![](https://i.imgur.com/Migwyw6.png)

![](https://i.imgur.com/zn42aa1.png)

查看完介紹與說明後，點擊「返回主選單」(或者輸入「主選單」) 回到主頁面。

## 查詢即時股價
即時爬取 Yahoo Finance 的股價資訊，點擊「查詢即時股價」快捷鍵，或者是輸入「即時股價」之後，bot 會提示接下來要輸入股價代號，如下面兩張圖:

![](https://i.imgur.com/wZdedOb.png)

![](https://i.imgur.com/agLSz4q.png)

例如: 接下來輸入 2337，查詢旺宏股價:

![](https://i.imgur.com/ZqnkfLa.png)

查詢完後，點擊「查詢股價詳細資訊」查看更深入的資訊，或者是「結束本次操作」，回到主畫面。

此處點擊「查詢股價詳細資訊」。

## 查詢股價詳細資訊
同樣也是即時爬取 Yahoo Finance 的股價資訊，但是提供更詳細的股價資訊，點擊「查詢詳細股價資訊」快捷鍵，或者是輸入「詳細股價」之後，bot 會提示接下來要輸入股價代號，如下面兩張圖:

![](https://i.imgur.com/z1p9PkJ.png)

![](https://i.imgur.com/I2DzhE8.png)

輸入股價代號來查詢詳細股價資訊，包括:
- 最新收盤價
- 開盤價
- 最高價
- 最低價
- 價差
- 漲跌幅
- 近五日平均價格
- 近五日標準差

例如: 輸入 2379，查詢瑞昱的詳細股價資訊:

![](https://i.imgur.com/elnWppw.png)

點擊「返回主選單」，回到主畫面。

## 查詢收盤價震盪圖
收盤價震盪圖指的是當天收盤價和開盤價之間的價格差，此功能會顯示歷史到現在的震盪圖:

![](https://i.imgur.com/UgydIk1.png)

![](https://i.imgur.com/ew5DFU2.png)

此處以 2498，也就是宏達電為例:

![](https://i.imgur.com/4KfsHDu.png)

bot 會返回一張可以儲存在裝置的震盪圖 (不需要自己截圖)

![](https://i.imgur.com/KHk5m32.png)

查看完之後，可以點擊「返回主選單」，回到主畫面。

## FSM
最後一個功能，相對起來較為簡單，就是查看本次作業我所使用的 FSM 圖，在主選單中點擊「FSM」快捷鍵或是輸入「FSM」來進入查看 FSM 的 state:

![](https://i.imgur.com/p3yqwwi.png)

![](https://i.imgur.com/C9NzNrP.png)

bot 同樣會返回一張可以直接儲存在裝置，不需要自己截圖的 FSM 圖，另外也可以點擊「前往網頁查看圖片」會直接跳轉到 Imgur 查看。

查看完之後就可以點擊「返回主選單」，回到主畫面。

# Deploy
Deploy webhooks on Heroku.

## App Information
App Name: **crawler3c**

![](https://i.imgur.com/EnF06lX.png)

## Resources
![](https://i.imgur.com/iU2Zsin.png) 

![](https://i.imgur.com/wu48Ay4.png)

## Line Developer Webhook URL Connection
![](https://i.imgur.com/akiTnAR.png)


## Heroku CLI installation
- [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
curl https://cli-assets.heroku.com/install.sh | sh
```

## Connect to Heroku
1. Register Heroku: https://signup.heroku.com
2. Create Heroku project from website
3. CLI Login
```
heroku login
```

## Upload project to Heroku
1. Add local project to Heroku project (or you can build it)
```
heroku git:remote -a {HEROKU_APP_NAME}
```
2. Set buildpack(s) in Heroku (for `pygraphviz` usage)
```
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt
heroku buildpacks:add https://github.com/weibeld/heroku-buildpack-graphviz
```
You can use
```
heroku buildpacks
```
to check which buildpack has already installed:

3. Set Environment - Line Messaging API Secret Keys
```
heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
```
4. Upload project
```
git add .
git commit -m "<message>"
git push heroku master
```

5. Your Project is now running on Heroku!
- Webhook Url: `{HEROKU_APP_NAME}.herokuapp.com/callback`
- Debug Command: `heroku logs --tail --app {HEROKU_APP_NAME}`

## Reference
- [TOC-Project-2020](https://github.com/NCKU-CCS/TOC-Project-2020)
- [Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
- [【TA Q&A】Heroku and pygraphviz](https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz)
