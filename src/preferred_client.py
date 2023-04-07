from client import Client

class PreferredClient(Client):
    def __init__(self, name, password):
        super.__init__(name)
        self.password = password