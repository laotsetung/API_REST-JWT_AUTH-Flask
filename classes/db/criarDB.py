import sqlite3
import sys
from conexao import conexao
import hashlib

#Criptografar a senha
hash_object = hashlib.sha256()
#Converte o password para Byte e encoda
hash_object.update('admin'.encode())
#Pega o valor hex do metodo hash
senha = hash_object.hexdigest()

c = conexao()
con = c.con
cur = c.cur

#Criar a tabela de usuarios
tabela_usuarios = """CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(32) NOT NULL,
    senha VARCHAR(256) NOT NULL,
    flag VARCHAR(50) NOT NULL
)"""
cur.execute(tabela_usuarios)
con.commit()

#Cryptografar a senha e inserir usuario admin no banco
#senha = Criptografar().encriptar('admin')

add_user = f"INSERT INTO usuarios (usuario, senha, flag) VALUES('admin','{senha}','ATIVO')"

cur.execute(add_user)
con.commit()

con.close()