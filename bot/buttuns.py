from telebot import types

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Мои закупки')
    keyboard.add(button1,)
    return keyboard