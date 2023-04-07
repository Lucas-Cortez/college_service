from datetime import datetime

def get_time_now():
    return int(datetime.timestamp(datetime.now()))