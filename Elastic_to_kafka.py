from elasticsearch import Elasticsearch, helpers
import json
import time
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.20.0.2:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
es = Elasticsearch('http://elastic:changeme@172.21.0.2:9200/')
res = helpers.scan(
                client = es,
				scroll = '2m',
                query = {"query": {"match_all": {}}},
                index = "*monitoring*")
for i in res:
    j = json.dumps(i, indent=4, sort_keys=True)
    producer.send('test', j)
