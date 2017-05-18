import boto3
import pprint
import json
import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from datetime import datetime

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

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

