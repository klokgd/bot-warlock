import shelve
from telebot import types
from sqlighter import sqlighter
from config import database_name, shelve_name

def count_rows():
    """
    Данный метод считает общее количество строк в базе данных и сохраняет в хранилище.
    Потом из этого количества будем выбирать музыку.
    """
    db = sqlighter(database_name)
    rowsnum = db.count_rows()
    with shelve.open(shelve_name) as storage:
    	storage['rows_count'] = rowsnum

def get_rows_count():
    """
    Получает из хранилища количество строк в БД
    :return: (int) Число строк
    """
    with shelve.open(shelve_name) as storage:
        rowsnum = storage['rows_count']
    return rowsnum

