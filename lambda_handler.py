import json
from lambda_function import lambda_handler

# Simulate an event
event = {
    'phi': {
        'requestContext': {
            'http': {
                'method': 'GET',
                'path': '/phi/26'
            },
            'routeKey': 'GET /phi/{up_to_power}'
        },
        'pathParameters': {
            'up_to_power': '26'
        }
    },
    'phi_power': {
        'requestContext': {
            'http': {
                'method': 'GET',
                'path': '/phi_power/4'
            },
            'routeKey': 'GET /phi_power/{power}'
        },
        'pathParameters': {
            'power': '4'
        }
    },
    'recip': {
        'requestContext': {
            'http': {
                'method': 'GET',
                'path': '/recip/7'
            },
            'routeKey': 'GET /recip/{denom}'
        },
        'pathParameters': {
            'denom': '7'
        }
    },
    'pythag': {
        'requestContext': {
            'http': {
                'method': 'GET',
                'path': '/pythag/1'
            },
            'routeKey': 'GET /pythag/{corner}'
        },
        'pathParameters': {
            'corner': '1'
        }
    },
    'dc': {
        'requestContext': {
            'http': {
                'method': 'GET',
                'path': '/dc/7'
            },
            'routeKey': 'GET /dc/{denom}'
        },
        'pathParameters': {
            'denom': '7'
        }
    }
}

# Call the Lambda function handler
result = lambda_handler(event.get('phi_power'), None)

body = json.loads(result.get('body'))
# Print the result
print(json.dumps(body, indent=4))

