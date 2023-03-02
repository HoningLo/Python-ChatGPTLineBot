# Python-ChatGPTLineBot

## **Installation**

### **Git Clone** Command

1. Open Git Bash.
2. Clone.

```bash
git clone https://github.com/HoningLo/Python-ChatGPTLineBot.git
cd Python-ChatGPTLineBot
```

### **Requirements**

- Python >= 3.7

Create a virtual environment:

```bash
python -m venv .venv
.venv\scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

- Apply for OpenAI API key: [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys)

Open the **appsettings.json** file and update the configuration values it contains to reflect the `OUR_LINE_CHANNEL_ACCESS_TOKEN`, `YOUR_LINE_CHANNEL_SECRET` and `YOUR_CHATGPT_TOKEN` for your cognitive services resource. Save your changes.

![Untitled](figure/Untitled.png)

## Execute

Run the app:

```bash
python app.py
```

Browse to the sample application at `http://localhost:5000` in a web browser.

![Untitled](figure/Untitled%201.png)

## ****Deploy your application code to Azure****

To create Azure resources in VS Code, you must have the [Azure Tools extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack) installed and be signed into Azure from VS Code.

In the application folder, open VS Code:

```bash
code .
```

Locate the Azure icon in the left-hand toolbar. Select it to bring up the Azure Tools for VS Code extension.

If you do not see the Azure Tools icon, make sure you have the Azure Tools extension for VS Code installed.

In the Azure Tools extension for VS Code:

1. Login
2. Find the **RESOURCES** section and select your subscription.
3. Check out the App Service you have created.

![Untitled](figure/Untitled%202.png)

Deploy your application code.

![Untitled](figure/Untitled%203.png)

![Untitled](figure/Untitled%204.png)

Browse to the deployed application in your web browser at the URL `http://<app-name>.azurewebsites.net`. If you see a default app page, wait a minute and refresh the browser.

![Untitled](figure/Untitled%205.png)

## Configure LINE WebHooks

Copy `https URL`.

![Untitled](figure/Untitled%206.png)

Paste Your `<https URL>/callback` before verifying.

![Untitled](figure/Untitled%207.png)

Verification successful.

![Untitled](figure/Untitled%208.png)

# Reference

[isdaviddong/chatGPTLineBot (github.com)](https://github.com/isdaviddong/chatGPTLineBot)

[https://beta.openai.com/docs/api-reference/completions/create](https://beta.openai.com/docs/api-reference/completions/create)

[line/line-bot-sdk-python: LINE Messaging API SDK for Python (github.com)](https://github.com/line/line-bot-sdk-python)

[ngrok - Online in One Line](https://ngrok.com/)

[https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/concepts/models](https://learn.microsoft.com/zh-tw/azure/cognitive-services/openai/concepts/models)

[Quickstart: Deploy a Python (Django or Flask) web app to Azure - Azure App Service | Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)
