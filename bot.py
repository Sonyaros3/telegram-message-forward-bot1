from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import asyncio

BOT_TOKEN = "8013086637:AAEn1aTPpkg4wuSSIclgcuLev48MUGBEvtI"
TARGET_USER_ID = 167546408

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_message:
        message_text = update.effective_message.text or "[Mesaj boş]"
        chat = update.effective_chat
        sender = update.effective_user

        chat_name = chat.title or "Özel Sohbet"
        sender_name = sender.full_name if sender else "Bilinmeyen"
        sender_username = f"@{sender.username}" if sender and sender.username else "(kullanıcı adı yok)"
        sender_id = sender.id if sender else "Bilinmiyor"

        iletilecek_mesaj = (
            f"📥 Yeni Mesaj\n"
            f"👥 Grup: {chat_name}\n"
            f"🙋 Gönderen: {sender_name} {sender_username}\n"
            f"🆔 Kullanıcı ID: {sender_id}\n"
            f"💬 Mesaj:\n{message_text}"
        )

        await context.bot.send_message(chat_id=TARGET_USER_ID, text=iletilecek_mesaj)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    print("✅ Bot çalışıyor... Render uyumlu mod aktif.")
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())
