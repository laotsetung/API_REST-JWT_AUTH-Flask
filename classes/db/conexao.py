import sqlite3

class conexao:

    con = None
    cur = None

    def __init__(self):
        try:
            self.con = sqlite3.connect('database.db')
            self.cur = self.con.cursor()
        except:
            print("Erro ao conectar na database.")