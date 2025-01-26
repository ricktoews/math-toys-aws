import json
from lambda_function import lambda_handler
from test_events import event

# Call the Lambda function handler
result = lambda_handler(event.get('dc'), None)

body = json.loads(result.get('body'))
# Print the result
print(json.dumps(body, indent=4))

