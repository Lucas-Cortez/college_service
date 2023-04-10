from utils.set_interval import Interval
from service_system import ServiceSystem
from password_generator import PasswordGenerator

if __name__ == '__main__':
    password_generator = PasswordGenerator()

    service = ServiceSystem(password_generator)

    service.new_client('Joao', 'normal')
    service.new_client('Diego', 'normal')
    service.new_client('Heduardo', 'preferencial')
    service.new_client('Daniel', 'preferencial')
    service.new_client('Adrian', 'normal')
    service.new_client('Gabriel', 'normal')
    service.new_client('Gustavo', 'normal')
    service.new_client('Lucas', 'preferencial')
    service.new_client('Matheus', 'preferencial')


    Interval.infinite(service.exec_routine, 1)