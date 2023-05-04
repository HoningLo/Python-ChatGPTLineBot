# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:20:42 2022

@author: lo
"""
# from dotenv import load_dotenv
import os
import requests
import json

def chatGPT(prompt, chatGPT_token):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {chatGPT_token}'
               } 
    data = {
        "model": "gpt-3.5-turbo-0301",
        "messages": [{"role":"system",
                      "content":"You are an AI assistant helping people find information.\
                      Chinese is represented by the language code zh-Hant.\
                      English is represented by the language code en-US."}
                      ] + prompt,
        "temperature":0.7,
        "max_tokens":800,
        "top_p":0.95,
        "frequency_penalty":0,
        "presence_penalty":0,
        "stop":None
        }
    response = requests.post(url, data = json.dumps(data), headers=headers)
    print(response.status_code)
    return response.json()["choices"][0]["message"]

if __name__ == "__main__":
    from MessageMemory import Memory

    # Get Configuration Settings
    folder_path = os.path.dirname(os.path.abspath(__file__))
    CONFIG = json.load(open(f"{folder_path}/../appsettings.json", "r"))
    chatGPT_token = CONFIG["OpenAI"]["CHATGPT_TOKEN"]
    memory = Memory(maxlen=5)

    # Run
    while True:
        # Get the input message from the user
        msg=str(input("Enter Your Message:"))

        # Add the human message to the memory
        memory.add_message({"role": "user", "content": f"{msg}"})

        # Generate a prompt based on the memory
        prompt = memory.generate_prompt()

        # Get the answer from the GPT-2 chatbot
        answer = chatGPT(prompt, chatGPT_token)
        print(answer["content"].strip())

        # Add the AI's response to the memory
        memory.add_message(answer)

        print(memory.generate_prompt())

