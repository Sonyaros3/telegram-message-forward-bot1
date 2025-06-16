from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Bot Token'ınız
BOT_TOKEN = "8013086637:AAEn1aTPpkg4wuSSIclgcuLev48MUGBEvtI"

# Mesajları ileteceğimiz Telegram Kullanıcı ID'niz
TARGET_USER_ID = 167546408

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        message_text = update.effective_message.text or "[Mesaj boş]"
        chat = update.effective_chat
        sender = update.effective_user

        chat_name = chat.title or "Özel Sohbet"
        sender_name = sender.full_name
        sender_username = f"@{sender.username}" if sender.username else "(kullanıcı adı yok)"
        sender_id = sender.id

        iletilecek_mesaj = (
            f"📥 Yeni Mesaj\n"
            f"👥 Grup: {chat_name}\n"
            f"🙋 Gönderen: {sender_name} {sender_username}\n"
            f"🆔 Kullanıcı ID: {sender_id}\n"
            f"💬 Mesaj:\n{message_text}"
        )

        await context.bot.send_message(chat_id=TARGET_USER_ID, text=iletilecek_mesaj)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

print("✅ Bot çalışıyor... Detaylı mesaj iletimi açık.")
app.run_polling()
