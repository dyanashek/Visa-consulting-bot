# Question-answer telegram bot
## Изменить язык: [Русский](README.md)
***
A simple chatbot that provides advice on frequently asked questions.
## [DEMO](README.demo.md)
## [LIVE](https://t.me/spain_pomogator_bot)
## Commands:
**For convenience, it is recommended to add these commands to the side menu of the bot using [BotFather](https://t.me/BotFather).**
- menu - displays the start menu
## Functionality:
1. Navigation menu to answer the most popular questions
2. Notification of the manager about the desire to sign up for a consultation
## Installation and use:
- Create an .env file containing the following variables:
> the file is created in the root folder of the project
   - specify the bot's telegram token in the file:\
   **TELEGRAM_TOKEN**=TOKEN
   - Bot ID (numbers in the token):
   **BOT_ID**=ID
   - **MANAGER_ID** contains the ID of the user who will receive notifications about abandoned orders. (for example: MANAGER_ID=1234)
- in the config.py file, assign your values to the variables:\
**WHATSAPP_PHONE** (Whatsapp phone number)\
**PHONE** (contact phone number)\
**TELEGRAM_MANAGER** (manager's nickname in telegram)\
**TELEGRAM_CHANNEL** (link to telegram channel)\
**WEBSITE** (site address)
- create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate # for mac
source venv/Scripts/activate # for windows
```
- install dependencies:
```sh
pip install -r requirements.txt
```
- run the project:
```sh
python3 main.py
```