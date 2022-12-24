from telegram.ext import CallbackContext
from telegram import Update
from anecAPI import anecAPI
import time, math
from logger import write_log

def get_joke(update: Update, context: CallbackContext):
    write_log(update, context)
    after_command = context.args
    print(after_command)
    update.message.reply_text(anecAPI.random_joke()) #.modern_joke())


def get_message(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if 'прив' in message: 
        update.message.reply_text(f'Взаимно Приветствую!') 
        return None 
    update.message.reply_text(f'вы ввели: {message},\n я не понял, что вы хотите сделать\nнажмите /help, чтобы узнать, что я умею.')  


def hello_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nПосчитаем?')


def help_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum - складываю два числа\n/sub - вычитаю второе число из первого\n/prod - перемножаю числа\n/div - делю первое число на второе\n/pow - возвожу первое число в степень второго\n/sqrt - извлекаю корень из введенного числа\n\nКоманду и числа вводите через пробел (десятичный разделитель - .)!\n/joke - рассказываю анекдот(иногда 18+)')


def time_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'{time.ctime(time.time())}')  #{datetime.datetime.now().time()}


def sum_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else:
        items = message.split() # /sum 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} + {y} = {round(x + y), 6}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def sub_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else:
        items = message.split() # /sub 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} - {y} = {round(x - y), 6}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def prod_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else:
        items = message.split() # /prod 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} * {y} = {round(x * y, 6)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def div_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else: 
        items = message.split() # /div 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} : {y} = {round(x/y, 6)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')
            

def pow_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else:
        items = message.split() # /pow 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x}^{y} = {round(x**y, 6)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')
     

def sqr_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message: 
        update.message.reply_text(f'Некорректный ввод. Десятичный разделитель - . (точка!). Вы ввели {message}')
    else:
        items = message.split() # /pow 123 534543
        if len(items) != 2:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')    
        elif not items[1].isalpha():
            x = float(items[1])    
            update.message.reply_text(f'корень из {x} = {round(math.sqrt(x), 6)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')
     