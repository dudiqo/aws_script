#
# Python script to get resource data from AWS API Gateaway
#
# Required libraries: boto3, argparse, json, csv
# Place credentials file in ~/.aws/credentials

from pprint import pprint
import boto3, argparse, json, csv

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

# Generates json file
def generate_json(apis, resources):
    for api in apis:
        i = 0
        full_output = {}
        output  = {
            'id': api['id'],
            'name': api['name'],
            'description': api['description'],
            'resources': 'resources'
        }
        full_output.update({i:output})
        i += 1

    with open("resources.json", "w") as write_file:
         json.dump(output, write_file)
    
    return full_output

# Generates json pretty file
def generate_json_pretty():
    obj = None
    with open('resources.json') as f:
        obj = json.load(f)

    outfile = open('resources.json', "w")
    outfile.write(json.dumps(obj, indent=4, sort_keys=True))
    outfile.close()

# Generate CSV file
def generate_csv(dictionary):
    with open('resources.csv','w') as f:
        w = csv.writer(f)
        w.writerows(dictionary.items())

# Main
def main():
    pass

args = prepare_args()
connection = connect(args)
apis = get_apis(connection)
resources = list_resources(connection, apis)


#pprint(resources)
#pprint(resources)
#json = generate_json(apis, resources)
#generate_json_pretty(json)
#pprint(generate_json(apis, resources))
pprint(resources)


#response = api_client.get_deployments(restApiId='n2nrifq6mg')
#print(response)