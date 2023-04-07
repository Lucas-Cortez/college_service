from client import Client

class NormalClient(Client):
    def __init__(self, name, password):
        super.__init__(name)
        self.password = password
        
