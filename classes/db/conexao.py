import sqlite3
from pathlib import Path
from os.path import dirname, realpath, join

class conexao:

    con = None
    cur = None

    def __init__(self):
        try:           
            APP_DIR = Path(dirname(realpath(__file__)))

            self.con = sqlite3.connect(join(APP_DIR, "database.db"))
            self.cur = self.con.cursor()
        except:
            print("Erro ao conectar na database.")