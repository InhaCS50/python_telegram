from telebot import TeleBot, types 
from text_to_speach import text_to_speech, speech_to_text

TOKEN = '6207499987:AAHHf2eGlF1bwKbrKOIj1FR9t65ZcGIHE_E'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    answer = f'<b>Salom!</b> {message.from_user.first_name}'
    bot.send_message(message.chat.id, text=answer, parse_mode='html')

@bot.message_handler(commands=['speech'])
def duck(message):
    text = ' '.join(message.text.split(' ')[1:])
    text_to_speech(text)
    with open('text_to_speech.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)

@bot.message_handler(content_types=['voice'])
def duck(message):
    file = bot.get_file(message.voice.file_id)
    bytes = bot.download_file(file.file_path)
    with open('voice.ogg', 'wb') as f:
        f.write(bytes)
    text = speech_to_text()
    bot.send_message(message.chat.id, text=text)


if __name__ == '__main__':
    bot.polling(none_stop=True)