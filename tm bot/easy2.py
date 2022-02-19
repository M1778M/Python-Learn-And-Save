import os
import telebot
from telebot import *
TOKEN = os.getenv('API_KEY')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['great'])
def great(message):
    bot.reply_to(message,"Tank You!")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message,"hello")



bot.polling()