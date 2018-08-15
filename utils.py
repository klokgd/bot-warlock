import shelve
from telebot import types
from random import shuffle
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

def generate_answer(answer):
    """
    Создаем массив для верного отображения из базы данных
    """
    answers = '{}'.format(answer)
    # Создаем лист (массив) и записываем в него все элементы
    list_items = []

    for item in answers:
        list_items.append(item)

    print(list_items[0])
    # Заполняем разметку перемешанными элементами

    return message


