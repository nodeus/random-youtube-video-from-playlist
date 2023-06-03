# Random youtube video from playlist telegram bot

Random YouTube video link from playlist using [YouTube Data API v3](https://console.developers.google.com), [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot), *requests*, *random* and *urlllib* written in Python.

Бот для телеграмма, по команде /video выдаёт случайное видео из определенного плейлиста.
Настройки в файле configtb.py — ключ Google API, токен бота телеграмма и ID плейлиста в YouTube. 

## Prerequisites
Google Developer Key for YouTube</br>
key = 'YOUR_DEVELOPER_KEY'</br>
</br>
YouTube playlist ID</br>
playlist_id = 'YOUTUBE PLAYLIST ID'</br>
</br>
Your telegram bot token, get it from @BotFather</br>
api_token = 'TELEGRAM BOT TOKEN'</br>
</br>
Google APIs Client Library</br>
pip3 install --upgrade google-api-python-client</br>
</br>
Python Telegram Bot</br>
pip3 install --upgrade python-telegram-bot</br>
</br>
Requests</br>
pip3 install --upgrade requests
