from client import Client
from utils.get_time_now import get_time_now
from abc import ABC, abstractmethod
from queue import Queue
class Balcony(ABC):
    start_service_time = None
    client_served = None
    served_time = None

    def _next_client(self, client: Client):
        self.start_service_time = get_time_now()
        
        client.answered()
        self.client_served = client

    @abstractmethod
    def next_client(self, queue: Queue, auxQueue: Queue):
        pass

