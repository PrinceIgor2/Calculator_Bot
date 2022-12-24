from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN 
from bot_command import *


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', help_command)
help_handler = CommandHandler('help', help_command)
hello_handler = CommandHandler('hello', hello_command)
sum_handler = CommandHandler('sum', summation_command)
sub_handler = CommandHandler('sub', substraction_command)
prod_handler = CommandHandler('prod', multiplication_command)
div_handler = CommandHandler('div', division_command)
joke_handler = CommandHandler('joke', get_joke)


message_handler = MessageHandler(Filters.text, get_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(prod_handler)
dispatcher.add_handler(div_handler)
dispatcher.add_handler(joke_handler)



dispatcher.add_handler(message_handler)

print('сервер запущен')
updater.start_polling()
updater.idle()