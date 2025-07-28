import telebot
from flask import Flask, request
from telebot import types

API_TOKEN = '8318157161:AAH4xklAtiJHtIUphDj4VtAsIF2th5-X8FA'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(name)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Bot is working!")

@app.route('/', methods=['POST'])  # 👈 Webhook route (required)
def webhook():
    update = types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200

if name == "main":
    app.run(host="0.0.0.0", port=5000)
