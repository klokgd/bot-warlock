import config
import telebot
import random
from sqlighter import sqlighter
import os
import time
import utils
from telebot import types, apihelper
import telegram
from telegram.ext import Updater

apihelper.proxy = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}


bot = telebot.TeleBot(config.token)

#get_Updates(offset, limit, timeout):

restricted_messages = ["Варлок", "варлок", "Вхуриндар", "угнетать", "угнетают", "либерал", "либерализм", "варлуша", "варлоша"]

@bot.message_handler(regexp="([Вв]ар[лок|луша|лоша]|[WwVv]arlo[ck|k]|[Вв]хуриндар)")
def get_answer(message):
	message.chat.type = 'group'
	print(message.chat.type)
	db_worker = sqlighter(config.database_name)
	row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
	bot.reply_to(message, row[0].format(message.text))
	db_worker.close()

@bot.message_handler(commands="start")
def hello(message):
	bot.send_message(message.chat.id, "хуй соси")

if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)