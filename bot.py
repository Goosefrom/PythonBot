import config, telebot
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я бот студради першого гуртожитку", reply_markup=markup)
@bot.message_handler(commands=["help"])
def help (message):
    bot.send_message(message.chat.id, config.HELP, reply_markup=markup)
@bot.message_handler(commands=['list'])
def list(message):
    bot.send_message(message.chat.id, config.PATH, reply_markup=markup)
@bot.message_handler(commands=['vodka'])
def vodka(message):
    bot.send_message(message.chat.id, 'канєшно залітайте', reply_markup=markup)
@bot.message_handler(commands=['feedback'])
def feed(message):
    bot.send_message(message.chat.id, 'Ваші пропозиції та скарги щодо розвитку бота - @goose_from', reply_markup=markup)
@bot.message_handler(commands=['water'])
def water(message):
    bot.send_message(message.chat.id, 'Скарги на воду - @liwikruk', reply_markup=markup)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
feedbut = types.KeyboardButton('/feedback')
helpbut = types.KeyboardButton('/help')
listbut = types.KeyboardButton('/list')
waterbut = types.KeyboardButton('/water')
markup.add(listbut, helpbut, waterbut, feedbut)
if __name__ == "__main__":
    bot.polling()
