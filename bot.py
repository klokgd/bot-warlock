import config
import telebot
import random
from sqlighter import sqlighter
import os
import time
import utils
from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(func=lambda message: True, regexp="([Вв]ар[лок|луша|лоша]|[WwVv]arlo[ck|k]|[Вв]хуриндар)")
def get_answer(message):
	db_worker = sqlighter(config.database_name)
	row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
	bot.forward_message(to_chat_id, from_chat_id, row[0])
	db_worker.close()

if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)