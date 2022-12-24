from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN #хранится в файл config.py (не выкладываю)
from bot_command import *


updater = Updater(TOKEN)
dispetcher = updater.dispatcher

hello_handler = CommandHandler('hello', hello_command)
joke_handler = CommandHandler('joke', get_joke)
start_handler = CommandHandler('start', help_command)
help_handler = CommandHandler('help', help_command)
time_handler = CommandHandler('time', time_command)
sum_handler = CommandHandler('sum', sum_command)
sub_handler = CommandHandler('sub', sub_command)
prod_handler = CommandHandler('prod', prod_command)
div_handler = CommandHandler('div', div_command)
pow_handler = CommandHandler('pow', pow_command)
sqr_handler = CommandHandler('sqrt', sqr_command)

message_handler = MessageHandler(Filters.text, get_message)

dispetcher.add_handler(joke_handler)
dispetcher.add_handler(hello_handler)
dispetcher.add_handler(time_handler)
dispetcher.add_handler(start_handler)
dispetcher.add_handler(help_handler)
dispetcher.add_handler(sum_handler)
dispetcher.add_handler(sub_handler)
dispetcher.add_handler(prod_handler)
dispetcher.add_handler(div_handler)
dispetcher.add_handler(pow_handler)
dispetcher.add_handler(sqr_handler)

# last dispetcher
dispetcher.add_handler(message_handler)

print('сервер запущен')
updater.start_polling()
updater.idle()