#Este arquivo é responsavel por Encode, Decode e Return do Token JWT
import time
import jwt
import os
from dotenv import load_dotenv, dotenv_values

JWT_SECRET = os.getenv("CHAVE")
JWT_ALGORITHM = os.getenv("ALGORITIMO")

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
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except:
        return None
