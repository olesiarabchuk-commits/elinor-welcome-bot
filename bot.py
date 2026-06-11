from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from flask import Flask
import os
import threading

TOKEN = os.getenv("BOT_TOKEN")

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for user in update.message.new_chat_members:
            await update.message.reply_text(
                f"👋 Вітаємо, {user.first_name}!\n\n"
                f"Раді бачити вас у спільноті майстрів Elinor 💜"
            )

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.run_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)
