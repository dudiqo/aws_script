#
# Python script to get resource data for AWS API Gateaway
#
# Required libraries: boto3
# Place credentials file in ~/.aws/credentials

from pprint import pprint
import boto3

# Establishes session and client connection
session = boto3.Session(profile_name='default')
credentials = session.get_credentials()
api_client = session.client('apigateway', region_name='us-east-1')

# Gets ids for available APIs
def get_ids():
    items = api_client.get_rest_apis()['items']
    ids = []
    for item in items:
        ids.append(item['id'])
    return ids

#Gets information about specific APIs
def get_api_info():
    api_ids = get_ids()
    for api in api_ids:
        api_info = api_client.get_rest_api(restApiId=api)
        pprint(api_info['name'])

# Lists resources from API
def list_resources():
    api_ids = get_ids()
    for api in api_ids:
        resource_list = api_client.get_resources(restApiId=api)
        #pprint(resource_list['items'])
        #return resource_list['items']
    for i in resource_list['items']:
        print(i['path'])



print(get_ids())
list_resources()

#response = api_client.get_deployments(restApiId='n2nrifq6mg')
#print(response)