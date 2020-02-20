import json

# Generates json file as dict --- cannot interate
def generate_json(apis, resources, connection):
    full_output = {}
    for api in apis:
        resource_list = connection.get_resources(restApiId=api['id'])
        reso = resource_list['items']
        output  = {
            'api_id': api['id'],
            'name': api['name'],
            'description': api['description'],
            'resources': reso
        }
        full_output.update(output)

    with open("resources.json", "w") as write_file:
        json.dump(full_output, write_file)
    
    return full_output

# Generates json with resource
def generate_json(apis, resources):
    api_resources = []
    i = 0
    for r in resources:
        res = {
        'id': r[i]['id'],
        'path': r[i]['path'],
        'resourceMethods': r[i]['resourceMethods']
        }
        api_resources.append(res)
        i += 1

    for api in apis:
        full_output = {}
        output  = {
            'id': api['id'],
            'name': api['name'],
            'description': api['description'],
            'resources': api_resources
        }
        full_output[api] = output

    # with open("resources.json", "w") as write_file:
    #     json.dump(output, write_file)



        res_full = []
        res = {
        'id': r[i]['id'],
        'path': r[i]['path'],
        'resourceMethods': r[i]['resourceMethods']
        }
        print(res)
        #res_full.update({r[i]['id']:res})
        res_full.append(res)
        i += 1
    return res_full