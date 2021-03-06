import json
import time
from elasticsearch import Elasticsearch, RequestsHttpConnection
#from config import settings
#ES_HOST = "http://35.154.96.13:9200/"


ES_HOST = "http://127.0.0.1:9200/"

ES_CLIENT = Elasticsearch(
    [ES_HOST],
    connection_class=RequestsHttpConnection,
    http_auth=('elastic', 'flyrobe123'),
)


def dump_elasticsearch_data():
    page = 2500000
    details_web = []
    query = {
      "size": 100000,
      "from": 1 * page,
      "query": {
        "match": {
          "event": "Details Web"
        }
      }
    }
    es_data = ES_CLIENT.search(index="fly", doc_type="users", body=query)
    details_web = details_web + es_data['hits']['hits']
      #time.sleep(3)
    with open('/home/ubuntu/user_mixpanel_data/mix_panel_data_details_web'+str(page)+'.json', 'wt') as outfile:
        json.dump(details_web, outfile)

dump_elasticsearch_data()