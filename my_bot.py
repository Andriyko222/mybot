import requests
import telebot
from telebot import types
from key import keyy
from tem import min,max



#keyboard кнопки
@bot.message_handler(commands=['start'])
def keybatton(message):
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("exchange rate💲")
    item2 = types.KeyboardButton("weather")
    m.add(item2)
    bot.send_message(message.chat.id, f"Hello!,{message.from_user.first_name}",reply_markup=m)


#інлайн кнопки валюта
def inlvalue():
    vel = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("USD",callback_data="Dolar")
    button2 = types.InlineKeyboardButton("EUR",callback_data="Euro")
    button3 = types.InlineKeyboardButton("PLN",callback_data="zlot")
    button4 = types.InlineKeyboardButton("CHF",callback_data="Franc")
    button5 = types.InlineKeyboardButton("GBP",callback_data="Funt")
    vel.add(button,button2,button3,button4,button5)
    return vel

#інлайн кнопки час
def inltime():
    tm = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Kyiv",callback_data="tmkyiv")
    button2 = types.InlineKeyboardButton("Tokyo",callback_data="tmtokyo")
    button3 = types.InlineKeyboardButton("Los Angeles",callback_data="tmla")
    button4 = types.InlineKeyboardButton("New York",callback_data="tmny")
    tm.add(button)
    return tm



@bot.message_handler(content_types=['text'])
def messaga(message):
    if message.text == "exchange rate💲":
        bot.send_message(message.chat.id, "choose currency", reply_markup=inlvalue())
    if message.text == "weather":
        bot.send_message(message.chat.id,"choose city", reply_markup=inltime())


    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "tmkyiv":
            bot.send_message(message.chat.id,min)
            bot.send_message(message.chat.id,max)



bot.polling(none_stop=True)