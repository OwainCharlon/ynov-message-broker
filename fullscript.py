from pykafka import KafkaClient
import confluent_kafka.admin, pprint
import numpy as np
import json
import time

sample_size = 7
std = 2
mean = 5

client = KafkaClient(hosts='127.0.0.1:9092')

# kafka_admin = confluent_kafka.admin.AdminClient({'bootstrap.servers': 'localhost:9092'})

# new_topic = confluent_kafka.admin.NewTopic('topic100', 1, 1)

# kafka_admin.create_topics([new_topic,])

for tp in client.topics:
    print(tp)

topic = client.topics['topic100']

with topic.get_sync_producer() as producer:
    count = 0
    while True:
        producer.produce( bytes( json.dumps({
            'id' : count,
            'payload' : np.array_str( np.random.normal(mean, std, sample_size) )
            }), encoding='UTF-8') )
        count += 1
        time.sleep(1)

consumer = topic.get_simple_consumer()

for message in consumer:
    if message is not None:
        print( type(message.value.decode("UTF-8")) )
        print( type( json.dumps(message.value.decode("UTF-8")) ) )
        dic = json.loads( json.dumps(message.value.decode("UTF-8")) )
        print( dic )
        for i in dic["payload"]:
            print( i )
