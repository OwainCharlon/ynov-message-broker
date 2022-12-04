from pykafka import KafkaClient
import confluent_kafka.admin, pprint
import numpy as np
import json
import time
import ast
client = KafkaClient(hosts='localhost:9092')

topic = client.topics['topic1001']

vect2_consumer = topic.get_simple_consumer()

for message in vect2_consumer:
    if message is not None:
        producer_msg = json.loads(message.value)
        print( json.dumps({
            'id' : producer_msg["id"],
            'type' : producer_msg["type"],
            'vect2' : [ producer_msg["payload"][x + 1] - producer_msg["payload"][x] for x in range( len(producer_msg["payload"]) -1 ) ]
            }).encode('utf-8'))