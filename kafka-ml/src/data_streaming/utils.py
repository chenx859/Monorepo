import logging
import socket

from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

from settings import KAFKA_BROKER


def create_producer():
    """
    this function creates a producer in kafka to producer data to . 

    Returns:
        producer: kafka producer 
    """
    try:
        producer = Producer({"bootstrap.servers": KAFKA_BROKER,
                             "client.id": socket.gethostname(),
                             "enable.idempotence": True,  # EOS processing
                             "compression.type": "lz4",
                             "batch.size": 64000,
                             "linger.ms": 10,
                             "acks": "all",  # Wait for the leader and all ISR to send response back
                             "retries": 5,
                             "delivery.timeout.ms": 1000})  # Total time to make retries
    except Exception as e:
        logging.exception("Couldn't create the producer")
        producer = None
    return producer


def create_consumer(topic, group_id):
    """
    this function creates a consumer to consume data from a topic .

    Returns:
        producer: kafka consumer 
    """
    try:
        consumer = Consumer({"bootstrap.servers": KAFKA_BROKER,
                             "group.id": group_id,
                             "client.id": socket.gethostname(),
                             "isolation.level": "read_committed",
                             "default.topic.config": {"auto.offset.reset": "latest", # Only consume new messages
                                                      "enable.auto.commit": False}
                             })

        consumer.subscribe([topic])
    except Exception as e:
        logging.exception("Couldn't create the consumer")
        consumer = None

    return consumer

def create_topic(topic, num_partitions, replication_factor):
    # Configuration: Replace 'localhost:9092' with your Kafka broker's address
    config = {'bootstrap.servers': 'localhost:9092'}

    # Create an AdminClient
    admin_client = AdminClient(config)
    # Create a NewTopic object
    new_topic = NewTopic(topic, num_partitions=num_partitions, replication_factor=replication_factor)

    # Create the topic
    fs = admin_client.create_topics([new_topic])

    # Wait for each operation to finish
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")
    return 