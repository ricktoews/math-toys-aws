from core import process_requests

def lambda_handler(event, context):
    return process_requests(event)
