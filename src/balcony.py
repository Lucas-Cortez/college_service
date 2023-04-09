from abc import ABC, abstractmethod
from queue import Queue
from random import randint

from client import Client
from utils.logger import Logger


def rand():
    return randint(0, 2)


class Balcony(ABC):
    client_served = None
    served_time = None
    closed_balcony = False

    def __init__(self, tag: str):
        self.tag = f'balcao {tag}'

    def _next_client(self, client: Client):
        self.served_time = rand() * 60
        
        client.answered()
        self.client_served = client

    def _close(self):
        self.closed_balcony = True

    @abstractmethod
    def next_client(self, queue: Queue, auxQueue: Queue, logger: Logger):
        pass

