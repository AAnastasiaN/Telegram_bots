import telebot
from telebot import types

bot = telebot.TeleBot('5988224050:AAGjrn1_ZtMRelJsW77tMV0Akhv_ukw4hw4')

# отслеживание команд

@bot.message_handler(commands=['start'])

def start(message):
    # вывод пользователя
    mess = f' Hi, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# обработка текста

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "И тебе hi", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id} ", parse_mode='html')
    elif message.text == "photo":
        photo = open('1622037833_24-phonoteka_org-p-ogon-piksel-art-krasivo-40.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

# обработка документов

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Cool!')


# создание кнопок

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти", url="https://fireguys.ru/apps/post-bezopasnosti-gdzs/normativy.html"))
    bot.send_message(message.chat.id, 'Иди на сайт!', reply_markup=markup)

# создание кнопок внизу

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('site')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "site", reply_markup=markup)

bot.polling(none_stop=True)