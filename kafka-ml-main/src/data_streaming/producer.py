import json
import random
import time
from datetime import datetime ,timedelta 
import numpy as np
from settings import TRANSACTIONS_TOPIC, DELAY
from utils import create_producer 
_id = 0
producer = create_producer()
# Define the start date and time
start_date = datetime(2014, 2, 28, 14, 25, 0)
# Define the time interval (5 minutes)
time_interval = timedelta(minutes=5)
# Start an infinite loop
counter = 0

if producer is not None:
    while True:
        timestamp = start_date + counter * time_interval  # Calculate timestamp
        value = np.random.uniform(0, 10)  # Generate a random value
        # Display the timestamp and value
        print(f"Timestamp: {timestamp}, Value: {value}")
        timestamp=timestamp.strftime("%Y-%m-%d %H:%M:%S")
        record = {"timestamp": timestamp , "value": value }
        record = json.dumps(record).encode("utf-8")
        counter += 1  # Increment the counter
        producer.produce(topic=TRANSACTIONS_TOPIC,
                         value=record)
        producer.flush()
        _id += 1
        time.sleep(DELAY)