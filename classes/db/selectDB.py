from conexao import conexao

c = conexao()
con = c.con
cur = c.cur

sql = "SELECT * FROM usuarios"

print(sql)
cur.execute(sql)

res = cur.fetchall()

for a in res:
    print(a)