import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ✅ إعدادات
logging.basicConfig(level=logging.INFO)
TOKEN = "توكن البوت هنا"
PASSWORD = "Asdf@1234$1234$"

# ✅ المتغيرات
allowed_users = set()  # لتخزين المستخدمين اللي دخلوا الباسورد

# ✅ دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in allowed_users:
        await update.message.reply_text("مرحباً بك من جديد 🎉")
    else:
        await update.message.reply_text("🔐 من فضلك أدخل كلمة السر للمتابعة:")

# ✅ التحقق من كلمة السر
async def check_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message_text = update.message.text

    if user_id in allowed_users:
        await update.message.reply_text("✅ أنت بالفعل مصرح لك بالدخول.")
        return

    if message_text == PASSWORD:
        allowed_users.add(user_id)
        await update.message.reply_text("✅ تم التحقق من كلمة السر! الآن يمكنك استخدام البوت.")
    else:
        await update.message.reply_text("❌ كلمة السر غير صحيحة. حاول مرة أخرى.")

# ✅ تشغيل التطبيق
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_password))

    app.run_polling()
