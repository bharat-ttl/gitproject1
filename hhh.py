from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

d = es.search(index='tata-parts-sample', body={
    "query": {
        "bool": {
            "should": [
                {
                    "multi_match": {
                        "query": "DCCARBURISING",
                        "fields": [
                            "part_number",
                            "desc_text",
                            "desc_text._2gram",
                            "desc_text._3gram",
                            "line_2",
                            "line_2._2gram",
                            "line_2._3gram",
                        ],
                        "fuzziness": "2",
                    }},
            ],
        },
    },
    "size": 7,
})

for i in d['hits']['hits']:
    print(i['_source'])
