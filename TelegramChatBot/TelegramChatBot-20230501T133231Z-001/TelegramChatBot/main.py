from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "6131331187:AAFfBdg7Gjm4gBQ4KLrRBLADtNfsvzv3RGk"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello my bot! ;)")

def run():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("Start", start))
    application.add_handler(CommandHandler("Help", start))

    application.run_polling()


if __name__ == "__main__":
    run()