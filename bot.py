from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
import asyncio

TOKEN = os.getenv("BOT_TOKEN")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for user in update.message.new_chat_members:
            await update.message.reply_text(
                f"👋 Вітаємо, {user.first_name}!\n\n"
                f"Раді бачити вас у спільноті майстрів Elinor 💜"
            )

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

asyncio.run(main())
