import boto3
import pprint
import json

client = boto3.client('es')

response = client.create_elasticsearch_domain(DomainName="turbo-es-domain-nbm1",
                        ElasticsearchClusterConfig={
                                'InstanceType': 't2.medium.elasticsearch',
                                'InstanceCount': 1,
                                'DedicatedMasterEnabled': False,
                                'ZoneAwarenessEnabled': False
		        },
                        EBSOptions={
                            'EBSEnabled': True,
                            'VolumeType': 'standard',
                            'VolumeSize': 10
                        },
			AccessPolicies='''{
			  "Version": "2012-10-17",
			  "Statement": [
			    {
			      "Effect": "Allow",
			      "Principal": {
				"AWS": [
				  "*"
				]
			      },
			      "Action": [
				"es:*"
			      ],
			      "Resource": "arn:aws:es:us-east-1:170873904690:domain/turbo-es-domain-nbm1/*"
			    }
			  ]
			}'''
	)	

with open('domain.json', 'w') as outfile:
    json.dump(response, outfile)
