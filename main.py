import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# إعدادات
logging.basicConfig(level=logging.INFO)

TOKEN = "توكن البوت هنا"
PASSWORD = "Asdf@1234$1234$"

# قائمة المستخدمين المسموح لهم
AUTHORIZED_USERS = set()
WAITING_FOR_PASSWORD = set()

# أمر البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        await update.message.reply_text("مرحباً بك من جديد! ✅")
    else:
        WAITING_FOR_PASSWORD.add(user_id)
        await update.message.reply_text("🔐 من فضلك أدخل كلمة السر للمتابعة:")

# التحقق من كلمة السر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if user_id in WAITING_FOR_PASSWORD:
        if text == PASSWORD:
            AUTHORIZED_USERS.add(user_id)
            WAITING_FOR_PASSWORD.remove(user_id)
            await update.message.reply_text("✅ تم التحقق! أهلاً بك في البوت.")
        else:
            await update.message.reply_text("❌ كلمة السر غير صحيحة. حاول مرة أخرى.")
    elif user_id in AUTHORIZED_USERS:
        await update.message.reply_text("👋 أنت بالفعل مسجل! تابع الأخبار هنا.")
    else:
        await update.message.reply_text("🔐 من فضلك ابدأ بـ /start.")

# تشغيل التطبيق
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
