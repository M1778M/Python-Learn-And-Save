import telebot
import time

TOKEN = "TOKEN"

bot = telebot.TeleBot(token=TOKEN)

def find_at(msg):
    for i in msg:
        if "@" in i:
            return i

@bot.message_handlers(command=['start'])
def send_wellcome(message):
    bot.reply_to(message,"Wellcom Bro")

@bot.message_handlers(command=['help'])
def help_user(message):
    bot.reply_to(message,"HELP_Command Start \n /get {line} \n you can use @")

@bot.message_handlers(func = lambda msg: msg.text is not None and '@' in msg.text)
def at_jo(message):
    text = message.text.split()
    at_text = find_at(text)

    bot.reply_to(message,"http://instagram.com/{}".format(at_text[1:]))

@bot.message_handlers(command=['get'])
def ret(message):
    bot.reply_to(message,"HACK-TIME")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)

