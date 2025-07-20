import logging
import requests
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# تقدر تغير التوكن ده بتوكن البوت الجديد بتاعك
TOKEN = "8152219074:AAEIPC-JJQuxat6UhYBWm04Y6KEO6kJb_Rs"

# إعداد اللوج
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# دالة لجلب الأخبار من API (مثال)
def get_forex_news():
    # تقدر تبدّل الرابط ده بـ API حقيقية أو ملف ثابت
    return "📰 Morning News:\n- Gold is rising due to geopolitical tensions.\n- USD is weak ahead of CPI data.\n- Oil prices remain stable.\n\n📊 Market Sentiment: Risk-off.\n\n#Gold #Forex #News"

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Gold News Bot!\nUse /news to get the latest market news."
    )

# أمر /news
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_text = get_forex_news()
    await update.message.reply_text(news_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))

    print("✅ Bot is running...")
    app.run_polling()
