import logging
import telegram
from telegram import (ReplyKeyboardMarkup,ReplyKeyboardRemove)
from telegram.ext import (Updater,CommandHandler,MessageHandler,Filters,ConversationHandler)
import os


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - $(massage)s",level=logging.INFO)

logger = logging.getLogger(__name__)

LOCATION,PHOTO,NAME,SERCING,TIME,ISTRUE = range(6)

reply_keybord = [["Start Again", "True"]]
markup = ReplyKeyboardMarkup(reply_keybord,resize_keyboard=True,one_time_keyboard=True)
TOKEN = "bot token"

PORT = os.environ.get("PORT",443)

bot = telegram.Bot(token=TOKEN)
chat_id = "chanel url or @chanel_name"

def start(update,context):
    user = update
    print(user)

def main():
    updater = Updater(TOKEN,use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start()))

    updater.start_webhook(listen='0.0.0.0',port=PORT,url_path=TOKEN)

    updater.bot.set_webhook('http://127.0.0.1:4040/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()