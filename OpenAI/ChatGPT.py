# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:20:42 2022

@author: lo
"""
# from dotenv import load_dotenv
import os
import requests
import json

def chatGPT(user, msg, chatGPT_token):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {chatGPT_token}'
               } 
    data = {
        "model": "gpt-3.5-turbo-0301",
        "messages": [{"role": f"{user}", "content": f"{msg}"}],
        "max_tokens": 4000,
        "temperature": 0.3,
        "top_p": 1,
        "presence_penalty":0,
        "frequency_penalty":0.5
        }
    response = requests.post(url, data = json.dumps(data), headers=headers)
    print(response.status_code)
    return response.json()["choices"][0]["message"]["content"].strip()


if __name__ == "__main__":
    # Get Configuration Settings
    folder_path = os.path.dirname(os.path.abspath(__file__))
    CONFIG = json.load(open(f"{folder_path}/../appsettings.json", "r"))
    chatGPT_token = CONFIG["OpenAI"]["CHATGPT_TOKEN"]

    # Run
    user = "user"
    msg="Say this is a test"
    answer = chatGPT(user, msg, chatGPT_token)
    print(answer)

