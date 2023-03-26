import datetime
import random

import telebot
from telebot import TeleBot, types


from config import BOT_TOKEN

from wb_parser import parse

bot = TeleBot(token=BOT_TOKEN)

# loaded file class
class File:
    name = ''
    info = ''
    def __init__(self):
        name = ''
        info = ''

# Marketplace class
# class Marketplace:
#     name = ''
#     def __init__(self):
#         name = ''


@bot.message_handler(content_types=['document'])
def save(message):
    # Save file sent by user
    file_info = bot.get_file(message.document.file_id)
    File.name = message.document.file_name

    src = 'files/' + File.name
    with open(src, 'wb') as new_file:
        new_file.write(bot.download_file(file_info.file_path))

    # Marketplace buttons
    markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add('Wildberries', 'Ozon', 'YandexMarket')
    msg = bot.send_message(message.chat.id,'Выберите маркетплейс', reply_markup=markup)
    bot.register_next_step_handler(msg, handle_docs)

def handle_docs(message):
    # bot choose marketplace
    bot.send_message(message.chat.id, f'Вы выбрали маркетплейс {message.text}')

    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Файл получен! Выполняется парсинг'), parsing(message))
def parsing(message):
    # Newfilename for file with parsed data
    newfilename = f'{File.name}_result_{datetime.datetime.now()}'.replace('.xlsx', '').replace(' ','-')

    # Parse data
    try:
        parse(srcfilename=f'files/{File.name}', filename=f'files/{newfilename}.xlsx', columnname='code')

    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то не так с файлом, попробуйте изменить файл и попробовать  снова')

    # Send parsed data
    try:
        bot.send_document(message.chat.id, open(rf'files/{newfilename}.xlsx', 'rb'))
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то не так с файлом, попробуйте изменить файл и попробовать  снова')

if __name__ == "__main__":
    bot.polling()
