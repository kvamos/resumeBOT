import config

import telebot
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)

print(1)

@bot.message_handler(commands=['start'])
def start (msg):
    markup_inline = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text = f'я ищу работу' , callback_data = 'work')
    item2 = types.InlineKeyboardButton(text = f'создать \n резюме' , callback_data = 'write')
    item3 = types.InlineKeyboardButton(text = f'редактировать \n резюме' , callback_data = 'redact')
    item4 = types.InlineKeyboardButton(text = f'информация' , callback_data = 'info')
    item5 = types.InlineKeyboardButton(text = f'удалить \n резюме' , callback_data = 'delite')
    markup_inline.add(item1 , item2 , item3 , item4 , item5)

    bot.send_message (msg.chat.id, f'привет я помогу тебе найти стажировку или работы😊' , 
                     reply_markup= markup_inline)
    

@bot.message_handler(commands = ['help'])
def help (msg):
    bot.send_message(msg.chat.id, 'msg.chat.id')













while True:
    try:
        bot.polling(none_stop=True)
        print(2)
    except Exception as e:
        print(e)
        time.sleep(15)
print('end')