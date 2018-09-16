import config
import telebot
import random
from sqlighter import sqlighter
import utils
from telebot import types, apihelper
import time
import re

apihelper.proxy = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}

bot = telebot.TeleBot(config.token, skip_pending=True)

reg = "(^| )[Вв]ар|лок|луша|лоша|]|(^| )[WwVv]arlo|(^| )[Ввх]уриндар|(^| )[Хх]ейтер|(^| )[Рр]абота|(^| )[Пп]рактика|(^| )[Мм]аг|(^| )[Уу]гнета|(^| )([Лл]иберал)|(^| )[Вв]уки|(^| )[Рр]епорт|(^| )срач|(^| )патворкинг|(^| )[Рр]усал|(^| )[Фф]еи"


@bot.message_handler(content_types="text")
def get_answer(message):
    db_worker = sqlighter(config.database_name)
    row = db_worker.select_single(random.randint(1, utils.count_rows()))
    match = re.search(reg, message.text)
    if match:
        # time.sleep(random.randint(15, 60))
        bot.reply_to(message, row[0].format(message.text))
    elif message.reply_to_message.from_user.id == bot.get_me().id:
    # time.sleep(random.randint(15, 60))
       bot.reply_to(message, row[0].format(message.text))

    # except:
    #	time.sleep(10)

    db_worker.close()


if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)
