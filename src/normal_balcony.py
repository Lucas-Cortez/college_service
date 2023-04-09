from balcony import Balcony

from normal_client import NormalClient
from preferred_client import PreferredClient
from queue import Queue
from utils.logger import Logger

class NormalBalcony(Balcony):
    def next_client(self, normalQueue: Queue[NormalClient], preferredQueue: Queue[PreferredClient], logger: Logger):
        if not normalQueue.empty():
            client = normalQueue.get()
            logger.log(f'Caixa {self.tag} normal solicitando cliente da fila normal {client.name}')
            self._next_client(client)
        elif not preferredQueue.empty():
            client = preferredQueue.get()
            logger.log(f'Caixa {self.tag} normal solicitando cliente da fila preferencial {client.name}')
            self._next_client(client)
        else:
            logger.log(f'Solicitando o fechamento do caixa normal {self.tag}')
            self._close()