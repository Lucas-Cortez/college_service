from balcony import Balcony
from password_generator import PasswordGenerator
from datetime import datetime
from random import randint
from queue import Queue

from preferred_balcony import PreferredBalcony
from normal_balcony import NormalBalcony

from preferred_client import PreferredClient
from normal_client import NormalClient

# print(datetime.timestamp(datetime.now()))
# print(datetime.timestamp(datetime.now()))

# opa = PasswordGenerator()
# print(opa.generatePassword())
# test = Balcony()
# test.get_next_client()

# opa = PreferredBalcony()

# print(isinstance(opa, Balcony))

# print('opa')

class Sistema():
    def __init__(self):
        self.normalBalconys = []
        self.preferredBalconys = []
        self.normalQueue = []
        self.preferredQueue = []
    




