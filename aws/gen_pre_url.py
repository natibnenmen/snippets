import boto3
import pprint
import json

client = boto3.client('es')


response = client.generate_presigned_url(ClientMethod='add_tags', Params={}, ExpiresIn=3600, HttpMethod='GET')

with open('presigned_url.txt', 'w') as outfile:
    outfile.write(response)
