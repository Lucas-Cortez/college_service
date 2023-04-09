from queue import Queue

from balcony import Balcony
from normal_client import NormalClient
from preferred_client import PreferredClient
from utils.logger import Logger

class PreferredBalcony(Balcony):
    def next_client(self, preferredQueue: Queue[PreferredClient], normalQueue: Queue[NormalClient], logger: Logger):
        if not preferredQueue.empty():
            client = preferredQueue.get()
            logger.log(f'Caixa {self.tag} preferencial solicitando cliente da fila preferencial {client.name}')
            self._next_client(client)
        elif not normalQueue.empty():
            client = normalQueue.get()
            logger.log(f'Caixa {self.tag} preferencial solicitando cliente da fila preferencial {client.name}')
            self._next_client(client)
        else:
            logger.log(f'Solicitando o fechamento do caixa preferencial {self.tag}')
            self._close()