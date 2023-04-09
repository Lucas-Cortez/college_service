from queue import Queue
from random import randint
from typing import List
from sys import exit

from balcony import Balcony
from preferred_balcony import PreferredBalcony
from normal_balcony import NormalBalcony

from client import Client
from preferred_client import PreferredClient
from normal_client import NormalClient

from password_generator import PasswordGenerator
from utils.get_time_now import get_time_now
from utils.logger import Logger

NORMAL = 'normal'
PREFERRED = 'preferencial'

MAX_WAIT_TIME = 1

def rand():
    return str(randint(1000, 9999))


class ServiceSystem():
    normalBalconys: List[NormalBalcony] = [NormalBalcony(rand()), NormalBalcony(rand()), NormalBalcony(rand())]
    preferredBalconys: List[PreferredBalcony] = [PreferredBalcony(rand()), PreferredBalcony(rand())]
    normalQueue: Queue[NormalClient] = Queue(maxsize=100)
    preferredQueue: Queue[PreferredClient]  = Queue(maxsize=100)
    logger = Logger()

    def __init__(self, password_generator: PasswordGenerator):
        self.password_generator = password_generator

    def new_client(self, name: str, service_type: str):
        if service_type == NORMAL:
            password = self.password_generator.generateNormalPassword()
            client = NormalClient(name, password)
            self.normalQueue.put(client)
            self.logger.log(f'Cliente {client.name} entrou na fila NORMAL com a senha {client.password}')
        elif service_type == PREFERRED:
            password = self.password_generator.generatePreferredPassword()
            client = PreferredClient(name, password)
            self.preferredQueue.put(client)
            self.logger.log(f'Cliente {client.name} entrou na fila PREFERENCIAL com a senha {client.password}')

    def __open_balcony(self, service_type: str):
        if service_type == NORMAL and len(self.normalBalconys) < 5:
            balcony = NormalBalcony(rand())
            self.normalBalconys.append(balcony)
            self.logger.log(f'Novo caixa NORMAL [{balcony.tag}] aberto')
        elif service_type == PREFERRED and len(self.preferredBalconys) < 2:
            balcony = PreferredBalcony(rand())
            self.preferredBalconys.append(balcony)
            self.logger.log(f'Novo caixa PREFERENCIAL [{balcony.tag}] aberto')

    def __close_system(self):
        self.logger.log(f"FIM DO LOG {40 * '='}")
        exit('Todos os clientes foram atendidos!')


    def __balconys_routine(self, balconys: List[Balcony], queue: Queue[Client], aux_queue: Queue[Client]):
        indexes_to_remove = []

        for i, balc in enumerate(balconys):
            if balc.client_served is None or (get_time_now() - balc.client_served.serviceTime) > balc.served_time:
                balc.next_client(queue, aux_queue, self.logger)
                
            if balc.closed_balcony:
                indexes_to_remove.append(i)

        for i in sorted(indexes_to_remove, reverse=True):
            if len(balconys) > 1:
                balconys.pop(i)


    def __clients_routine(self, queue: Queue[Client], service_type: str):
        for client in queue.queue:
            if (client.calculateWaitingTime() > MAX_WAIT_TIME * 60):
                self.logger.log(f'Pedido de abertura de novo caixa {service_type} enviado')
                self.__open_balcony(service_type)

    def exec_routine(self):
        if not self.normalBalconys[0].closed_balcony:
            self.__balconys_routine(self.normalBalconys, self.normalQueue, self.preferredQueue)
        if not self.preferredBalconys[0].closed_balcony:
            self.__balconys_routine(self.preferredBalconys, self.preferredQueue, self.normalQueue)

        self.__clients_routine(self.normalQueue, NORMAL)
        self.__clients_routine(self.preferredQueue, PREFERRED)

        if self.normalBalconys[0].closed_balcony and self.preferredBalconys[0].closed_balcony:
            self.__close_system()
