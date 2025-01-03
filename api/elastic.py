from elasticsearch import Elasticsearch
from services.productService import get_all_products
from elasticsearch.helpers import bulk

es = Elasticsearch("http://elastic:9200")

mapping = {
    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "russian"
            }
        }
    }
}
index_name = "abakarov"


def create_index():
    if not es.indices.exists(index=index_name, body=mapping):
        es.indices.create(index=index_name, body=mapping)


def delete_index():
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)


# поиск по всем полям
response = es.search(index="first_index", query={"match_all": {}})
print("Результаты поиска:")
for hit in response["hits"]["hits"]:
    print(f"ID: {hit['_id']}, Источник: {hit['_source']}")


def add_data_to_document():
    create_index()

    documents = []

    for item in get_all_products():
        document = {
            "_op_type": "index",
            "_index": index_name,
            "_id": item.id,
            "_source": {
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "quantity": item.quantity
            }
        }

        documents.append(document)

    bulk(es, documents)


def get_data(word):
    data = []
    response = es.search(
        index=index_name,
        query={"multi_match": {
            "query": word,
            "fields": ["name^3", "description"]
        }})

    for hit in response["hits"]["hits"]:
        data.append(hit['_source'])
        # print(f"ID: {hit['_id']}, Источник: {hit['_source']}")

    return data


