# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:20:42 2022

@author: lo
"""
# from dotenv import load_dotenv
import os
import requests
import json

def chatGPT(msg, chatGPT_token):
    url = "https://api.openai.com/v1/completions"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {chatGPT_token}'
               } 
    data = {
        "model": "text-davinci-003",
        "prompt": f"{msg}",
        "max_tokens": 4000,
        "temperature": 0.5
        }    
    response = requests.post(url, data = json.dumps(data), headers=headers)
    print(response.status_code)
    return response.json()["choices"][0]["text"]


if __name__ == "__main__":
    # Get Configuration Settings
    folder_path = os.path.dirname(os.path.abspath(__file__))
    CONFIG = json.load(open(f"{folder_path}/../appsettings.json", "r"))
    chatGPT_token = CONFIG["OpenAI"]["CHATGPT_TOKEN"]

    # Run
    msg="Say this is a test"
    answer = chatGPT(msg, chatGPT_token)
    print(answer)

