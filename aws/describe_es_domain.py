import boto3
import pprint
import json

client = boto3.client('es')

response = client.describe_elasticsearch_domain(
    DomainName='turbo-es-domain-2'
)

pprint.pprint(response)
#print json.load(response)['DomainStatus']['Endpoint']
print response['DomainStatus']['Endpoint']
