from abc import ABC, abstractclassmethod

class Client(ABC):
    def __init__(self, name):
        self.name = name
        # self.password = passwordGenerator.generatePassword()
        # self.isPreferred = isPreferred
        # if isPreferred:
        #     self.password = passwordGenerator.generatePreferredPassword()
        # else:
        #     self.password = passwordGenerator.generatePassword()
        
    @abstractclassmethod
    def get_password(self):
        pass

