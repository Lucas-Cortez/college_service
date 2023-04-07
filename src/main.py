from balcony import Balcony
from password_generator import PasswordGenerator
from datetime import datetime
from random import randint
from queue import Queue

from preferred_balcony import PreferredBalcony
from normal_balcony import NormalBalcony

from preferred_client import PreferredClient
from normal_client import NormalClient

NORMAL = 'normal'
PREFERRED = 'preferencial'

passwordGenerator = PasswordGenerator()


def generate_random_wait_time(a, b):
    return randint(a, b)

def rand():
    return generate_random_wait_time(0, 30)


class ServiceSystem():
    def __init__(self):
        self.normalBalconys = [NormalBalcony(), NormalBalcony(), NormalBalcony()]
        self.preferredBalconys = [PreferredBalcony(), PreferredBalcony()]
        self.normalQueue = Queue(maxsize=100)
        self.preferredQueue = Queue(maxsize=100)

    def new_client(self, name: str, service_type: str):
        if service_type == NORMAL:
            password = passwordGenerator.generateNormalPassword()
            client = NormalClient(name, password)
            self.normalQueue.put({ 'client': client, 'wait_time': rand() })
        elif service_type == PREFERRED:
            password = passwordGenerator.generatePreferredPassword()
            client = PreferredClient(name, password)
            self.preferredQueue.put({ 'client': client, 'wait_time': rand() })

    def open_balcony(self, service_type: str):
        if service_type == NORMAL and len(self.normalBalconys) < 5:
            self.normalBalconys.append(NormalBalcony())
        elif service_type == PREFERRED and len(self.preferredBalconys) < 2:
            self.preferredBalconys.append(PreferredBalcony())

    def close_balcony(self, service_type: str):
        if service_type == NORMAL and len(self.normalBalconys) > 1:
            self.normalBalconys.pop()
        elif service_type == PREFERRED and len(self.preferredBalconys) > 1:
            self.preferredBalconys.pop()


def exec_routine():
    