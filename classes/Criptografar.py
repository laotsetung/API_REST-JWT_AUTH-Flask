import hashlib

class Criptografar:

    def __init__(self) -> None:
        self.hash_object = hashlib.sha256()

    def encriptar(self, texto):
        #Converte o password para Byte e encoda
        self.hash_object.update(texto.encode())

        #Pega o valor hex do metodo hash
        hash_password = self.hash_object.hexdigest()
        
        return hash_password