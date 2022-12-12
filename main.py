# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:47:35 2022

@author: lo
"""

from dotenv import load_dotenv
import os

# import requests
# from datetime import datetime

from flask import Flask, request, abort
# import json, time

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from ChatGPT import chatGPT

# Get Configuration Settings
load_dotenv()
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
channel_secret = os.getenv('LINE_CHANNEL_SECRET')

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(f"{channel_access_token}")
# Channel Secret
handler = WebhookHandler(f"{channel_secret}")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=chatGPT(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(port=port, debug=True)


