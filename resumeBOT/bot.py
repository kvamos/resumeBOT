import config
import time

import telebot
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)

print(1)

@bot.message_handler(commands=['start'])
def start (msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("искать вакансии")
    btn2 = types.KeyboardButton("меню")
    markup.add(btn1 , btn2)
    markup_inline = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text = f'информация' , callback_data = 'info')
    item2 = types.InlineKeyboardButton(text = f'резюме' , callback_data = 'write')
    item3 = types.InlineKeyboardButton(text = f'советы' , callback_data = 'advice')
    item4 = types.InlineKeyboardButton(text = f'удалить резюме' , callback_data = 'delite')
    markup_inline.add(item1 , item2  , item3 , item4, )

    bot.send_message (msg.chat.id, 'Привет! 👋 ' , 
                     reply_markup = markup)
    bot.send_message (msg.chat.id, f'Я здесь, чтобы помочь тебе найти стажировки и работу во время и после учёбы в университете. Если ты ищешь возможности для практики или подработки, просто дай знать, и я помогу тебе с поиском! 🚀' , 
                     reply_markup = markup_inline)
    
    


@bot.callback_query_handler(func=lambda call: True)
def inline_button(call):
    if call.data == 'info':
        bot.send_message(call.message.chat.id, 'Привет! Я бот, который помогает тебе в поиске стажировок и работы во время и после учёбы в вузе. Моя задача — облегчить процесс поиска интересных вакансий и стажировок, предоставляя тебе актуальные предложения от компаний, которые ищут талантливых студентов и выпускников.'
'\nВот, что я могу сделать для тебя:'
'\n1. Поиск вакансий и стажировок: Я помогу найти предложения, соответствующие твоей специализации, уровню образования и интересам.' 
'\n2. Советы по составлению резюме: Я предоставлю рекомендации по созданию резюме и сопроводительных писем, чтобы ты мог выгодно выделиться среди других кандидатов.'
'\n3. Подготовка к собеседованию: Я поделюсь полезными советами и часто задаваемыми вопросами на собеседованиях, чтобы ты мог уверенно проходить интервью.'
'\n4. Информация о карьерных мероприятиях: Узнай о ярмарках вакансий, мастер-классах и других карьерных событиях, которые могут помочь в поиске работы.'
'\n5. Обратная связь и поддержка: Ты сможешь задать мне любые вопросы по поиску работы и стажировок, и я постараюсь дать наилучший ответ.')




while True:
    try:
        bot.polling(none_stop=True)
        print(2)
    except Exception as e:
        print(e)
        time.sleep(15)
print('end')