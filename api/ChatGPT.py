# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:20:42 2022

@author: lo
"""
from dotenv import load_dotenv
import os
import requests
import json

def chatGPT(prompt, chatGPT_token, model):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {chatGPT_token}'
               } 
    data = {
        "model": f"{model}",
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

def azure_chatGPT(prompt, chatGPT_token, model, azure_endpoint, deployment_name, api_version):
    url = f"{azure_endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"
    headers = {'Content-Type': 'application/json',
               'api-key': f'{chatGPT_token}'
               } 
    data = {
        "model": f"{model}",
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
    # folder_path = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(r"../.env", override=True)
    channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    channel_secret = os.getenv("LINE_CHANNEL_SECRET")
    chatGPT_token = os.getenv("CHATGPT_TOKEN")
    model = os.getenv("MODEL")
    is_azure_openai = bool(os.getenv("IS_AZURE_OPENAI"))
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")
    api_version = os.getenv("API_VERSION")
    memory = Memory(maxlen=5)

    # Run
    while True:
        # Get the input message from the user
        msg=str(input("Enter Your Message:"))

        # Add the human message to the memory
        memory.add_message({"role": "user", "content": f"{msg}"})

        # Generate a prompt based on the memory
        prompt = memory.generate_prompt()

        # Get the answer from the GPT chatbot
        if(is_azure_openai):
            answer = azure_chatGPT(prompt, chatGPT_token, model, azure_endpoint, deployment_name, api_version)
        else:
            answer = chatGPT(prompt, chatGPT_token, model)
        print(answer["content"].strip())

        # Add the AI's response to the memory
        memory.add_message(answer)

        print(memory.generate_prompt())

