from utils.set_interval import SetInterval
from service_system import ServiceSystem
from password_generator import PasswordGenerator

# Daniel Carlos de Siqueira Santos - RA: 109681
# Gabriel Tadeu Geromel - RA: 108818
# Gustavo Henrique Vitor - RA: 108837
# Heduardo Gabriel Costa - RA: 109439
# Lucas Cortez Sanches - RA: 110434

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


    SetInterval.infinite(service.exec_routine, 1)