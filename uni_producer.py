from pykafka import KafkaClient
import confluent_kafka.admin, pprint
import numpy as np
import json
import time

sample_size = 7
min_value = 2
max_value = 5

client = KafkaClient(hosts='127.0.0.1:9092')

#kafka_admin = confluent_kafka.admin.AdminClient({'bootstrap.servers': 'localhost:9092'})

#new_topic = confluent_kafka.admin.NewTopic('topic100', 1, 1)
# Number-of-partitions  = 1
# Number-of-replicas    = 1

#kafka_admin.create_topics([new_topic,])

for tp in client.topics:
    print(tp)

topic = client.topics['topic1001']

with topic.get_sync_producer() as producer:
    count = 0
    while True:
        producer.produce( json.dumps({
            'id' : count,
            'type' : 'uni',
            'payload' : np.array( np.random.uniform(min_value, max_value, sample_size) ).tolist()
            }).encode('utf-8')) 
        count += 1
        time.sleep(5)