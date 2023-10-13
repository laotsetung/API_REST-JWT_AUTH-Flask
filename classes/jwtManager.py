#Este arquivo é responsavel por Encode, Decode e Return do Token JWT
import time
import jwt

#Coloquei informações do projeto neste arquivo configSC
from classes.configSC import configSC

JWT_SECRET = configSC.secret
JWT_ALGORITHM = configSC.algorithm

#Essa função retorna os Tokens gerados.
def token_response(token: str):
    return {
        "access token" : token
    }

#Essa função gera o token com o userID (No caso para testes o Token tem o prazo de 1min de validade)
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 60
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

#Essa função decodifica o token (ou seja, valida o token recebido)
def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms='HS256')
        print (decode_token)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return None
