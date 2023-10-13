import sqlite3
#import mysql.connector

class conexao:

    con = None
    cur = None

    def __init__(self):
        self.con = sqlite3.connect('E:/TI/23/python/Flask/10-Flask_jwt_auth/dataBase/database.db')
        """self.con = mysql.connector.connect(
            host="localhost",
            user="sc_casatereza",
            password="a1d3mi8n@",
            database="sc_casatereza"
            )"""
        self.cur = self.con.cursor()