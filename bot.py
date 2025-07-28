from flask import Flask, request
import telebot
import requests

BOT_TOKEN = '8318157161:AAH4xklAtiJHtIUphDj4VtAsIF2th5-X8FA'
KOBOLD_API_URL = 'https://favourite-qualify-probe-centered.trycloudflare.com/v1'

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(name)

@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_text = message.text

    response = requests.post(KOBOLD_API_URL, headers={
        "Content-Type": "application/json"
    }, json={
        "model": "koboldcpp",  # or "gpt-3.5-turbo" if emulated
        "messages": [{"role": "user", "content": user_text}],
        "temperature": 0.7
    })

    reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
    bot.send_message(message.chat.id, reply)

# Setup webhook once
import requests
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url=https://your-webhook-url.com/")

# Run server
if name == 'main':
    app.run(port=5001)
