
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from news_fetcher import get_daily_news

TOKEN = "7916780567:AAEP9bZtqRjV1yZ8xwEiDANSOeu5yi3xnes"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! I’ll send you trading news regularly.")

async def send_news(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    news = get_daily_news()
    await context.bot.send_message(chat_id=chat_id, text=news)

async def schedule_jobs(app):
    # Schedule jobs for 3 AM, hourly, and important news alerts
    from datetime import time
    app.job_queue.run_daily(send_news, time(hour=3, minute=0))
    app.job_queue.run_repeating(send_news, interval=3600, first=10)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await schedule_jobs(app)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
