# Question-answer telegram bot
## Change language: [English](README.en.md)
***
Простой чат-бот, который предоставляет консультацию по часто задаваемым вопросам.
## [DEMO](README.demo.md)
## [LIVE](https://t.me/spain_pomogator_bot)
## Команды:
**Для удобства рекомендуется добавить данные команды в боковое меню бота, используя [BotFather](https://t.me/BotFather).**
- menu - выводит стартовое меню
## Функционал:
1. Навигационное меню для ответа на самые популярные вопросы
2. Уведомление менеджера о желании записаться на консультацию
## Установка и использование:
- Создайте файл .env, содержащий следующие переменные:
> файл создается в корневой папке проекта
  - в файле указать токен телеграмм бота:\
  **TELEGRAM_TOKEN**=ТОКЕН
  - ID бота (цифры в токене):
  **BOT_ID**=ID
  - в **MANAGER_ID** указан ID пользователя, которому будут приходить уведомления об оставленных заявках. (например: MANAGER_ID=1234)
- в файле config.py присвойте переменным ваши значения:\
**WHATSAPP_PHONE** (номер телефона WhatsApp)\
**PHONE** (контактный номер телефона)\
**TELEGRAM_MANAGER** (ник менеджера в telegram)\
**TELEGRAM_CHANNEL** (ссылка на telegram канал)\
**WEBSITE** (адрес сайта)
- создать и активировать виртуальную среду:
```sh
python3 -m venv venv
source venv/bin/activate # for mac
source venv/Scripts/activate # for windows
```
- установить зависимости:
```sh
pip install -r requirements.txt
```
- запустить проект:
```sh
python3 main.py
```