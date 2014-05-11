'''
Created on May 10, 2014
@author: jbarker
'''

# 
# 
# import elasticsearch as esearch
# 
# 
# es = esearch.Elasticsearch()
# 
# 
# es = esearch.Elasticsearch(["search1:9200","search2.9200"])
# 
# es = esearch.Elasticsearch(["search1:9200"],sniff_on_start=True)
# 
# es.index(
#          index="my_app",
#          doc_type="blog_post",
#          id=1,
#          body={
#                "title":"Elasticsearch clients",
#                "content":"Interesting content...."
# })
# 
# es.get(index="my_app", doc_type="blog_post", id=1)
# 
# 
# es.search(index="my_app", body={"query": {"match": {"title": "elasticsearch"}}})

# 
# from datetime import datetime
# from elasticsearch import Elasticsearch
# 
# # by default we connect to localhost:9200
# es = Elasticsearch()
# 
# # datetimes will be serialized
# es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
# {u'_id': u'42', u'_index': u'my-index', u'_type': u'test-type', u'_version': 1, u'ok': True}
# 
# # but not deserialized
# es.get(index="my-index", doc_type="test-type", id=42)['_source']
# {u'any': u'data', u'timestamp': u'2013-05-12T19:45:31.804229'}
# 
# from datetime import datetime
# from elasticsearch import Elasticsearch
# from pyes import *
# es = Elasticsearch(connection_class=ThriftConnection)
# 
# # create connection that will automatically inspect the cluster to get
# # the list of active nodes. Start with nodes 'esnode1' and 'esnode2'
# es = Elasticsearch(
#     ['esnode1', 'esnode2'],
#     # sniff before doing anything
#     sniff_on_start=True,
#     # refresh nodes after a node fails to respond
#     sniff_on_connection_fail=True,
#     # and also every 60 seconds
#     sniffer_timeout=60
# )

# connect to localhost directly and another node using SSL on port 443
# and an url_prefix
# es = Elasticsearch([
#     {'host': 'localhost'},
#     {'host': 'othernode', 'port': 443, 'url_prefix': 'es', 'use_ssl': True},
# ])
# 
# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime(2010, 10, 10, 10, 10, 10)
# }
# res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['created'])
# 
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])
# 
# es.indices.refresh(index="test-index")
# 
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])



from datetime import datetime
from elasticsearch import Elasticsearch

# by default we connect to localhost:9200
es = Elasticsearch(["Mit.elasticsearch.org:80"], sniff_on_start=False)

# datetimes will be serialized
es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
{u'_id': u'42', u'_index': u'my-index', u'_type': u'test-type', u'_version': 1, u'ok': True}

# but not deserialized
es.get(index="my-index", doc_type="test-type", id=42)['_source']
{u'any': u'data', u'timestamp': u'2013-05-12T19:45:31.804229'}










