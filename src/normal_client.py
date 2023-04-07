from client import Client

class NormalClient(Client):
    def __init__(self, name, passwordGenerator):
        super.__init__(name)
        self.password = passwordGenerator.generatePassword()
        
