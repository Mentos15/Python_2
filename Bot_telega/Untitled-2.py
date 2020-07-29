import telebot

bot = telebot.TeleBot('929699223:AAHZnanpAtG1TDepBUXTMrv-Ooas94c-eps')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ЧиПсеКи Lays', 'ЧиПсЕкИ Премьер')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привет Артик, Какие чипсики ты выберешь сегодня?', reply_markup=keyboard1)
    


bot.polling()