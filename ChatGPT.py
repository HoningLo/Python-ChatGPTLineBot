# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:20:42 2022

@author: lo
"""
from dotenv import load_dotenv
import os
import requests
import json

# Get Configuration Settings
load_dotenv()
chatGPT_token = os.getenv('CHATGPT_TOKEN')

def chatGPT(msg):
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
    msg="Say this is a test"
    answer = chatGPT(msg)
    print(answer)

