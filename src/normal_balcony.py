from balcony import Balcony
from queue import Queue

class NormalBalcony(Balcony):
    def next_client(self, normalQueue: Queue, preferredQueue: Queue):
        if not normalQueue.empty():
            self._next_client(normalQueue.get())
        elif not preferredQueue.empty():
            self._next_client(preferredQueue.get())