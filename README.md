# Telegram Bot on Render (Webhook Based)

This project lets you run a Telegram bot using Flask hosted for free on [Render.com](https://render.com).

---

## 📦 Files Structure

```
project/
├── bot.py                # Main bot logic using Flask + pyTelegramBotAPI
├── requirements.txt      # Python dependencies
└── README.md             # (You're here)
```

---

## 🔧 Requirements

* A Telegram bot token (from @BotFather)
* A free Render account
* A GitHub account (to host the code repo)

---

## 🧠 Python Dependencies (requirements.txt)

```
Flask
pyTelegramBotAPI
```

---

## 📜 bot.py (Overview)

* Sets a Flask webhook endpoint
* Handles incoming updates from Telegram
* Responds to `/start` command

---

## 🚀 Deployment on Render

### 1. Upload to GitHub

* Create a repo like `telegram-bot-render`
* Upload `bot.py` and `requirements.txt`

### 2. Setup on Render

* Go to [Render.com](https://render.com)
* Click **New Web Service**
* Connect GitHub, select your repo
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `python bot.py`
* Environment: Python 3, Port: `5000`

Render will provide a public HTTPS URL like:

```
https://your-bot-name.onrender.com
```

---

## 🤖 Webhook Setup

In `bot.py`, set the following:

```python
API_TOKEN = 'YOUR_BOT_TOKEN'
WEBHOOK_URL = 'https://your-bot-name.onrender.com/'
```

> The bot will auto-register webhook when it starts.

---

## ✅ Test Your Bot

* Open Telegram
* Search your bot
* Send `/start`
* You should receive a welcome message

---

## 📌 Notes

* This works on webhook only (not polling)
* You must set the correct public URL with HTTPS
* Render free tier sleeps after 15 min of inactivity, may need re-ping

---

## ✨ Credits

Created using [Flask](https://flask.palletsprojects.com/) + [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) + [Render](https://render.com)

---

Feel free to fork, improve, or reuse!
