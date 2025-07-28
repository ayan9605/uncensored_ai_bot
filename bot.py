from flask import Flask, request
import telebot

API_TOKEN = '8318157161:AAH4xklAtiJHtIUphDj4VtAsIF2th5-X8FA'
WEBHOOK_URL = 'https://eg-visual-suggestions-con.trycloudflare.com/'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your webhook-based bot.")

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Unsupported Media Type', 415

@app.route('/', methods=['GET'])
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host='0.0.0.0', port=5000)
