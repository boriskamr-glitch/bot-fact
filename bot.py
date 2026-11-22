import telebot
from confic import token
from logic import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["fact"])
def send_fact(message):
    random_fact = fact()
    bot.send_message(message.chat.id, random_fact)
    speak(random_fact)

bot.polling()