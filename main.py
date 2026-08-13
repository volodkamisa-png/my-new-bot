import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8992617197:AAFbwlHBWzilu1zLlIXfBVXNESWN3Rep-XQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Напиши мені опис музики, яку хочеш створити.")

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"🎶 Прийнято! Генерую трек за запитом: '{user_text}'...")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), generate))

if __name__ == "__main__":
    print("Бот запущений!")
    app.run_polling()
