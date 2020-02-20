from pprint import pprint

dict = {
    'position': 'string',
    'items': [
        {
            'id': 'string',
            'parentId': 'string',
            'pathPart': 'string',
            'path': 'string',
            'resourceMethods': {
                'string': {
                    'httpMethod': 'string',
                    'authorizationType': 'string',
                    'authorizerId': 'string',
                    'apiKeyRequired': True,
                    'requestValidatorId': 'string',
                    'operationName': 'string',
                    'requestParameters': {
                        'string': True
                    },
                    'requestModels': {
                        'string': 'string'
                    },
                    'methodResponses': {
                        'string': {
                            'statusCode': 'string',
                            'responseParameters': {
                                'string': True
                            },
                            'responseModels': {
                                'string': 'string'
                            }
                        }
                    },
                    'methodIntegration': {
                        'type': 'HTTP',
                        'httpMethod': 'string',
                        'uri': 'string',
                        'connectionType': 'INTERNET',
                        'connectionId': 'string',
                        'credentials': 'string',
                        'requestParameters': {
                            'string': 'string'
                        },
                        'requestTemplates': {
                            'string': 'string'
                        },
                        'passthroughBehavior': 'string',
                        'contentHandling': 'CONVERT_TO_BINARY',
                        'timeoutInMillis': 123,
                        'cacheNamespace': 'string',
                        'cacheKeyParameters': [
                            'string',
                        ],
                        'integrationResponses': {
                            'string': {
                                'statusCode': 'string',
                                'selectionPattern': 'string',
                                'responseParameters': {
                                    'string': 'string'
                                },
                                'responseTemplates': {
                                    'string': 'string'
                                },
                                'contentHandling': 'CONVERT_TO_BINARY'
                            }
                        }
                    },
                    'authorizationScopes': [
                        'string',
                    ]
                }
            }
        },
    ]
}

final = {
    'apiKeyRequired' : dict['items'][0]['resourceMethods']['string']['apiKeyRequired']
    }

pprint(final)