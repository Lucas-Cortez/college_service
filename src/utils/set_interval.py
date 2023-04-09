import threading

class Interval:
    def infinite(func, sec: float):
        e = threading.Event()
        while True:
            e.wait(sec)
            func()

    def max(func, sec: float, how_many: int):
        i = 0
        e = threading.Event()
        while i < how_many:
            i += 1
            e.wait(sec)
            func()