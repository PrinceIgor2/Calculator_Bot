from telegram.ext import CallbackContext
from telegram import Update
from anecAPI import anecAPI

def hello_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nХочешь, чтобы я посчитал за тебя?')


def get_message(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if 'прив' in message: 
        update.message.reply_text(f'Приветствую, если не шутишь!') 
        return None 
    update.message.reply_text(f'Ты ввел: {message},\n что желаешь сделать\nнажмите /help и я тебе помогу')  


def help_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    update.message.reply_text(f'/hello\n/help\n/sum - сложение\n/sub - вычитание\n/prod - умножение\n/div - деление\n\nВведи через пробел команду и числа(разделитель вещественного числа - точка)!\n/joke - анекдот(на любителя)')

def summation_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Неверно, дружок! Разделитель вещественного числа - точка, а ты ввел {message}')
    else:
        items = message.split() # /sum 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Неверно, дружок! Ты ввел {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} + {y} = {round((x + y),1)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Ты ввел {message}, это точно не цифры')


def substraction_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Неверно, дружок! Разделитель вещественного числа - точка, а ты ввел {message}')
    else:
        items = message.split() # /sub 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Неверно, дружок! Ты ввел {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} - {y} = {round((x - y), 1)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Ты ввели {message}, это точно не цифры')


def multiplication_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Неверно, дружок! Разделитель вещественного числа - точка, а ты ввел {message}')
    else:
        items = message.split() # /prod 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Неверно, дружок! Ты ввел {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} * {y} = {round((x * y), 1)}')
        else:
            update.message.reply_text(f'Неверно, дружок!Ты ввел {message}, это точно не цифры')


def division_command(update: Update, context: CallbackContext):
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Неверно, дружок! Разделитель вещественного числа - точка, а ты ввел {message}')
    else: 
        items = message.split() # /div 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Неверно, дружок! Ты ввел {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} : {y} = {round((x/y), 1)}')
        else:
            update.message.reply_text(f'Неверно, дружок! Ты ввел {message}, это точно не цифры')
            

     

def get_joke(update: Update, context: CallbackContext):
    after_command = context.args
    print(after_command)
    update.message.reply_text(anecAPI.random_joke()) #.modern_joke())