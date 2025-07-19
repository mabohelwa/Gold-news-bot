import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "7916780567:AAEP9bZtqRjV1yZ8xwEiDANSOeu5yi3xnes"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في GoldWithNossaBot!\n\n"
        "سأرسل لك الأخبار والتحليلات الذهبية هنا يوميًا.\n"
        "تابعني وانتظر المفاجآت 🟡✨"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
