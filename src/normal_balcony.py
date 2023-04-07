from balcony import Balcony
from datetime import datetime
from normal_client import NormalClient
from utils.get_time_now import get_time_now

class NormalBalcony(Balcony):
    start_service_time = None
    client_served = None

    def next_client(self, client: NormalClient):
        self.start_service_time = get_time_now()
        client.answered()
        self.client_served = client
