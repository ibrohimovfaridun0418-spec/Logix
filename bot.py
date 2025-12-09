from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "AAHETOeAhp__F3rQCe8Xidi57sFoYaHqOpc"
GROUP_ID = -1003414479883

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Yuk ma'lumotini yuboring, men uni chiroyli qilib guruhga tashlayman."
    )

def format_cargo(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    result = ""

    for line in lines:
        result += line + "\n\n"

    result += "➖➖➖➖➖➖➖➖➖➖"
    return result

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    formatted = format_cargo(text)

    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=formatted
    )

    await update.message.reply_text("Guruhga yuborildi! ✅")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()