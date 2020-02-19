#
# Python script to get resource data from AWS API Gateaway
#
# Required libraries: boto3, argparse
# Place credentials file in ~/.aws/credentials

from pprint import pprint
import boto3
import argparse
import json

# Gets parameters provided by the user
def prepare_args():
    parser = argparse.ArgumentParser(description='AWS resoruces')
    parser.add_argument('-p', '--profile', help="AWS credentials profile name", required=False, default='default')
    parser.add_argument('-r', '--region', help="AWS region", required=True)
    parser.add_argument('-m', '--methods', help="HTTP methods", required=False)
    parser.add_argument('-o', '--output', help="Output format", required=False, choices=['json', 'csv', 'json-pretty'])
    args = parser.parse_args()
    return args

# Establishes session and client connection
def connect(args):
    session = boto3.Session(profile_name=args.profile)
    api_client = session.client('apigateway', region_name=args.region)
    return api_client

# Lists APIs
def get_apis(connection):
    apis = connection.get_rest_apis()['items']
    return apis

# Lists resources from API
def list_resources(connection, apis):
    ids = [i['id'] for i in apis]
    resources = []
    for api in ids:
        resource_list = connection.get_resources(restApiId=api)
        resource = resource_list['items']
        resources.append(resource)
    return resources

# Generates json
def generate_json(apis, resources):
    for api in apis:
        i = 0
        full_output = []
        output  = {
            'id': api['id'],
            'name': api['name'],
            'description': api['description'],
            'resources': resources
        }
        full_output.append(output)
        i += 1
    
    with open("resources.json", "w") as write_file:
        json.dump(output, write_file)

    return full_output

# Generates pretty json
def generate_json_pretty(json_file):
    parsed = json.loads(json_file)
    pretty = json.dumps(parsed, indent=4, sort_keys=True)
    
    with open("resources_p.json", "w") as write_file:
        json.dump(pretty, write_file)


args = prepare_args()
connection = connect(args)
apis = get_apis(connection)
resources = list_resources(connection, apis)
#pprint(resources)
#json = generate_json(apis, resources)
#generate_json_pretty(json)
#pprint(generate_json(apis, resources))
json_file = generate_json(apis, resources)
generate_json_pretty(json_file)

#response = api_client.get_deployments(restApiId='n2nrifq6mg')
#print(response)