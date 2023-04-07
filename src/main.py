from balcony import Balcony
from preferred_balcony import PreferredBalcony
from password_generator import PasswordGenerator


# opa = PasswordGenerator()
# print(opa.generatePassword())
# test = Balcony()
# test.get_next_client()

opa = PreferredBalcony()

print(isinstance(opa, Balcony))

# print('opa')



