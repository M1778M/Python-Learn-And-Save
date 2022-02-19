import logging
import telegram
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, ConvertionHandler
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)

loc, photo, name, serving, time, confirmation = range(6)

reply_keyboard = [['Start Again','IsTrue'],
                  ['Test','Test','Test'],
                  ['NoneSpace']]


Markup = ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True,one_time_keyboard=True)
#--------------------
token = ''

bot = telegram.Bot(token)

channelId = ''



def start(update,context):
        user = update  # update.from_user -> info of user
        print(user)

def main():
    updater = Updater(token, use_context=True)
    
    dp = updater.dispacher

    dp.add_handler(CommandHandler('start',start))
    
    PORT = int(os.environ.get('PORT',443))

    updater.start_webhook(listen='0.0.0.0',port=PORT,url_path=token) # 0.0.0.0 = all ips
    updater.bot.set_webhook(f'https://address.adr/{token}')
    

    updater.idle() # CTRL-C TO STOP

main()
