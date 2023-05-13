import json

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

with open('lpt_p.json') as f:
    data = json.load(f)

for record in data:
    es.index(index='tata-parts-sample', id=record['part_number'], body=record)

print('total Records Count: ', len(data))
