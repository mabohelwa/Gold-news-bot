import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8152219074:AAEIPC-JJQuxat6UhYBWm04Y6KEO6kJb_Rs"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! I am your Gold News Bot.")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get("https://api.nossa.news/forex/gold")
        if response.status_code == 200:
            data = response.json()
            message = f"🟡 Gold News:\n\n{data.get('news', 'No news found')}"
        else:
            message = "Failed to fetch news from source."
    except Exception as e:
        message = f"Error: {str(e)}"

    await update.message.reply_text(message)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))

    print("✅ Bot is running...")
    app.run_polling()