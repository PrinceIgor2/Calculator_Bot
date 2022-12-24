from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN 
from bot_command import *


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', help_command)
help_handler = CommandHandler('help', help_command)
hello_handler = CommandHandler('hello', hello_command)
summation_handler = CommandHandler('sum', summation_command)
substraction_handler = CommandHandler('sub', substraction_command)
multiplication_handler = CommandHandler('prod', multiplication_command)
division_handler = CommandHandler('div', division_command)
joke_handler = CommandHandler('joke', get_joke)


message_handler = MessageHandler(Filters.text, get_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(summation_handler)
dispatcher.add_handler(substraction_handler)
dispatcher.add_handler(multiplication_handler)
dispatcher.add_handler(division_handler)
dispatcher.add_handler(joke_handler)



dispatcher.add_handler(message_handler)

print('сервер запущен')
updater.start_polling()
updater.idle()