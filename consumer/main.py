from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
   'message',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-0001',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['localhost:9094'])

for m in consumer:
    print(m.value)