import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8586777918:AAHRqGlnUR8ljNPLVcAf6Nq3ZzuN8zzAZ0Y"
ADMIN_ID = 8394486435  
GROUP_ID = -1003414479883  

bot = telebot.TeleBot(TOKEN)

PRICE = 15000  

cards = [
    ("Uzcard Z.Savarova", "5614 6835 1590 5578"),
    ("Uzcard F.Ibrohimov", "5614 6818 1929 1315")
]

@bot.message_handler(commands=['start'])
def start(msg):
    text = "Assalomu alaykum, botga xush kelibsiz!\n\nTez va oson yuk va mashina topishingiz mumkin!"
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton("Guruhga azo bo‘lish", url="https://t.me/LogiX_grup"))
    btn.add(InlineKeyboardButton("Kanalga azo bo‘lish", url="https://t.me/+7sCDtnwlNIkzZjUy"))
    btn.add(InlineKeyboardButton("To‘lov qilish", callback_data="pay"))
    bot.send_message(msg.chat.id, text, reply_markup=btn)

@bot.callback_query_handler(func=lambda c: True)
def callback(c):
    if c.data == "pay":
        text = "Botni ishga tushirish narxi: 15 000 so‘m.\n\nTo‘lov kartalari:"
        for name, number in cards:
            text += f"\n💳 *{name}:* `{number}`"
        bot.send_message(c.message.chat.id, text, parse_mode="Markdown")
        bot.send_message(c.message.chat.id, "To‘lov qilgach, checkni tashlang.")
    
    if c.data == "okbtn":
        bot.send_message(ADMIN_ID, f"Foydalanuvchi to‘lov qildi: {c.from_user.id}")

@bot.message_handler(content_types=['photo'])
def check(msg):
    if msg.reply_to_message and "check" in msg.reply_to_message.text.lower():
        bot.forward_message(ADMIN_ID, msg.chat.id, msg.message_id)
        bot.send_message(msg.chat.id, "Check yuborildi, tez orada tekshiriladi!")

bot.polling()