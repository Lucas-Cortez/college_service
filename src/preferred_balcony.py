from balcony import Balcony
from queue import Queue

class PreferredBalcony(Balcony):
    def next_client(self, preferredQueue: Queue, normalQueue: Queue):
        if not preferredQueue.empty():
            self._next_client(preferredQueue.get())
        elif not normalQueue.empty():
            self._next_client(normalQueue.get())