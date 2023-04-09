from abc import ABC, abstractmethod

from utils.get_time_now import get_time_now

class Client(ABC):
    def __init__(self, name: str, password: int):
        self.name = name
        self.password = password
        self.arrivalTime = get_time_now()
        self.serviceTime = None

    def calculateWaitingTime(self):
        if self.serviceTime is None:
            return get_time_now() - self.arrivalTime
        else:
            return self.serviceTime - self.arrivalTime
        
    def answered(self):
        self.serviceTime = get_time_now()

    @abstractmethod
    def log_client(self):
        pass

