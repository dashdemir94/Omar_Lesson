
import telebot

from  telebot import types

bot = telebot.TeleBot('6571234218:AAHiPlaD356fiZ04yjf0HJP15Q0ogDAt3IQ')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def url (message):
    print(message.text)
    bot.reply_to(message, 'Hi Omar, My name is Dashdemir')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)

    img = open('photo.jpeg', 'rb')
    bot.send_photo(message.from_user.id, img, caption=message.text)



bot.polling(non_stop=True, interval=0)
