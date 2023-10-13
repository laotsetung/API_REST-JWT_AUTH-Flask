from classes.db.conexao import conexao
from classes.Criptografar import Criptografar

class login:
           
    def verificaLogin(usuario :str, senha :str):
       
        senha = Criptografar().encriptar(senha)
        c = conexao()
                
        con = c.con
        cur = c.cur
                   
        sql = f"SELECT COUNT(id) FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
        cur.execute(sql)
        res = cur.fetchall()
        
        if res[0][0] == 1: #Se a somas dos ID selecionados for == 1 (Login correto!)
            con.close()
            return True
        else: #Se login errado e o count nao for 1
            con.close()
            return False 