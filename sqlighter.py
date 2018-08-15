import sqlite3

class sqlighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT message FROM warlock_message').fetchall()
    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT message FROM warlock_message WHERE id = ?', (rownum,)).fetchone()
    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT message FROM warlock_message').fetchall()
            return len(result)
    def close(self):
     	""" Закрываем текущее соединение с БД """
     	self.connection.close()

