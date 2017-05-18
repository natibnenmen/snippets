import boto3
import pprint
import json
import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from datetime import datetime
from time import gmtime, strftime

client = boto3.client('es')

response = client.describe_elasticsearch_domain(
    DomainName='turbo-es-domain-nbm1'
)

print response['DomainStatus']['Endpoint']
Endpoint = response['DomainStatus']['Endpoint']
print("Endpoint: {0}".format(Endpoint))

url = 'http://{0}:9200'.format(Endpoint)
print 'url: {0}'.format(url)

aws_access_key_id = ""
aws_secret_access_key = ""
REGION = response['DomainStatus']['ARN'].split(':')[3]
print("REGION: {}".format(REGION))

host = Endpoint
awsauth = AWS4Auth(aws_access_key_id, aws_secret_access_key, REGION, 'es')

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print("es.info: {0}".format(es.info()))

doc2 = '''{
    "author": "kimchy",
    "text": "Elasticsearch: cool. bonsai cool.",
    "@timestamp": "%s"
}'''

#'@timestamp': datetime.now(),

for i in range (10000, 10010):
  res = es.index(index="test-index", doc_type='tweet', id=i, body=json.loads(doc2 % strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())))
print(res['created'])


doc1 = '''{
  "directors": [
    "Tim Burton"
  ],
  "genres": [
    "Comedy",
    "Sci-Fi"
  ],
  "plot": "The Earth is invaded by Martians with irresistible weapons and a cruel sense of humor.",
  "title": "Mars Attacks!",
  "actors": [
    "Jack Nicholson",
    "Pierce Brosnan",
    "Sarah Jessica Parker"
  ],
  "year": 1996,
  "@timestamp": "%s"
}'''


for i in range(2000, 2005):
  res = es.index(index="test-index", doc_type='tweet', id=i, body=json.loads(doc1 % strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())))
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=3)
print(res['_source'])

es.indices.refresh(index="test-index")

