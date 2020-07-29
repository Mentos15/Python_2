import telebot
import config
import pyowm
from datetime import datetime, date, time

owm = pyowm.OWM('976e26b04c26bc61ef1a3f1ad17947ca', language="ru")
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temperature) + "\n"

    bot.send_message(message.chat.id, answer)

    while datetime.now().minute == 50:
        bot.send_message(message.chat.id, "HELLO")





bot.polling(none_stop=True)
