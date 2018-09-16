import shelve
from telebot import types
from sqlighter import sqlighter
from config import database_name

def count_rows():
    """
    Данный метод считает общее количество строк в базе данных и сохраняет в хранилище.
    Потом из этого количества будем выбирать музыку.
    """
    db = sqlighter(database_name)
    rowsnum = db.count_rows()
    return rowsnum



