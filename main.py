from telebot import TeleBot, types

TOKEN = '6207499987:AAHHf2eGlF1bwKbrKOIj1FR9t65ZcGIHE_E'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    answer = f'<b>Salom!</b> {message.from_user.first_name}'
    bot.send_message(message.chat.id, text=answer, parse_mode='html')

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, text=message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)