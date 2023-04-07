import threading

def set_interval(func, sec, howMany):
    i = 0
    e = threading.Event()
    while i < howMany:
        i += 1
        e.wait(sec)
        func()