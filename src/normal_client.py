from client import Client
from datetime import datetime
from utils.get_time_now import get_time_now

class NormalClient(Client):
    def __init__(self, name: str, password: int):
        super().__init__(name)
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
        
        
