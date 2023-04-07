from abc import ABC, abstractmethod, abstractproperty

class Balcony(ABC):

    @abstractmethod 
    def get_next_client(self):
        pass
        
        