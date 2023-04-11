from client import Client

class NormalClient(Client):
    def __init__(self, name: str, password: int):
        super().__init__(name, password)    
        
