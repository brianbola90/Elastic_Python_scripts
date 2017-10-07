from kafka import  KafkaConsumer
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
from elasticsearch import helpers
es = Elasticsearch('http://elastic:changeme@172.21.0.2:9200/')

consumer = KafkaConsumer(bootstrap_servers='172.20.0.2:9092',
                             auto_offset_reset='earliest')
consumer.subscribe(['test'])

id = 0

for message in consumer:
    id += 1
    actions = [
        {"_index": "new-index","_type": "doc",
    "_id": id ,
    "_source": {
        "field": "hello",
        "any": str(message),
        "timestamp": datetime.now() - timedelta(hours = 1)
        }
  }
]
    helpers.bulk(es, actions)
