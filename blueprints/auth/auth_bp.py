from flask import Blueprint, request
from classes.jwtManager import signJWT, decodeJWT
from classes.configSC import configSC
from classes.login import login

#Cria a blueprint de autenticação
auth_routes = Blueprint("auth_BluePrint", __name__, template_folder='templates')

#Rota para login - Verifica usuario e senha no banco de dados e gera um Token se eles forem corretos
@auth_routes.route("/login", methods=['POST'])
def auth_login():
    print(request.form)
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        print(f"debug: usuario:{usuario} / senha:{senha}")

        if login.verificaLogin(usuario,senha):
            return signJWT(usuario), 200
        else:
            return "Usuario ou Senha inválido, Permissão Negada!", 401
    else:
        return "Rota /login é esperada sendo metodo POST", 204


#Rota para testar se o Token é válido, ou seja, se foi fornecido por este app e se ainda não expirou
@auth_routes.route("/home", methods=['GET'])
def home():
    token = str(request.headers['Authorization'])
    token = token.split(' ')[1]
    
    if token:
        retorno = decodeJWT(token)
        if retorno == None:
            return "Token Inválido ou Expirado, fazer login novamente!", 401
        else:
            estudio = configSC().nomeEstudio
            return f"Logado na API REST do app : {estudio} ;  rota: /home", 200
    else:
        return "Token não fornecido, terminando!", 401
