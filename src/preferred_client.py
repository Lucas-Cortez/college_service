from client import Client

class PreferredClient(Client):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)

    def log_client(self):
        # Implementar o retorno das informações do cliente
        return print('preferencial') 
    