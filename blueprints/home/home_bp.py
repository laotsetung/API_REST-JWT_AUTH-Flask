from flask import Blueprint, request
from classes.jwtManager import decodeJWT
import os
from dotenv import load_dotenv, dotenv_values

home_routes = Blueprint('home_BluePrint', __name__, template_folder='templates')

#Rota para usar a aplicação (no caso uma rota de teste) - primeira rota da aplicação
@home_routes.route("/index")
def index():
    token = str(request.headers['Authorization'])
    token = token.split(' ')[1]
    
    if token:
        retorno = decodeJWT(token)
        if retorno == None:
            return "Token Inválido ou Expirado, fazer login novamente!", 401
        else:
            estudio = os.getenv("nomeApp")
            return f"Logado na API REST do app : {estudio} ; rota /index", 200
    else:
        return "Token não fornecido, requisição encerrada", 401
