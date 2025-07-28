
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8318157161:AAH4xklAtiJHtIUphDj4VtAsIF2th5-X8FA"

URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")
    payload = {"chat_id": chat_id, "text": f"Received: {text}"}
    requests.post(URL, json=payload)
    return {"ok": True}

@app.route("/", methods=["GET"])
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
