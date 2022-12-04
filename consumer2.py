from pykafka import KafkaClient
import confluent_kafka.admin, pprint
import numpy as np
import json
import time
import ast
client = KafkaClient(hosts='localhost:9092')

topic = client.topics['topic1001']

consumer2 = topic.get_simple_consumer()

for message in consumer2:
    if message is not None:
        #print(message.offset, message.value)
        #print(message.value.decode("utf-8"))
	    #print(producer_msgt(message.value.decode("UTF-8")))
        #print( type(message.value.decode("UTF-8")) )
        #print( type( json.dumps(message.value.decode("UTF-8")) ) )
        producer_msg = json.loads(message.value)
        print( message.value ) 



