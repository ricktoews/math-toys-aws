import json
import sys
sys.path.append('./modules')

from utils import normalize_event
from phi import phi_first_n
from calc_decimal import calc_decimal
from phi import get_phi
from pythag import get_pythag_by_corner

def lambda_handler(event, context):
    #print("====> Event object before normalization")
    #print(event)
    normalized_event = normalize_event(event)
    #print("====> normalized event object")
    #print(normalized_event)

    path = normalized_event.get('path', '')
    path_parameters = normalized_event.get('pathParameters', {})
    response = {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"}
    }
    desc = ''
    data = []

    route_handlers = {
        '/phi': handle_phi,
        '/dc': handle_dc,
        '/recip': handle_recip,
        '/pythag': handle_pythag,
        '/': handle_root
    }

    for route, handler in route_handlers.items():
        if path.startswith(route):
            return handler(response, path_parameters)

    
def handle_phi(response, path_parameters):
    power = path_parameters.get('power', 1)
    if power and power.isdigit():
        power = int(power)
        desc = f"phi to the power of {power}"
        data = get_phi(int(power))
        response['body'] = json.dumps({"description": desc, "data": data})
    else:
        response['statusCode'] = 400
        response['body'] = json.dumps({"error": "Invalid power parameter"}) 
    return response

def handle_dc(response, path_parameters):
    denom = path_parameters.get('denom', 1)
    if denom:
        denom = int(denom)
        desc = f"decimal expansion for denominator {denom}"
        data = []
        for num in range(1, denom):
            data.append(calc_decimal(num, denom, 10))
        response['body'] = json.dumps({"description": desc, "data": data})
    return response

def handle_recip(response, path_parameters):
    denom = path_parameters.get('denom', 1)
    if denom:
        denom = int(denom)
        desc = f"decimal expansion for reciprocal of {denom}"
        data = calc_decimal(1, denom, 10)
        response['body'] = json.dumps({"description": desc, "data": data})
    return response

def handle_pythag(response, path_parameters):
    corner = path_parameters.get('corner', 1)
    if corner:
        corner = int(corner)
        desc = f"Pythagorean triples where c - b = {corner}"
        data = get_pythag_by_corner(corner)
        response['body'] = json.dumps({"description": desc, "data": data})
    return response

def handle_root(response, path_parameters):
    response['statusCode'] = 404
    response['body'] = json.dumps({"description": "Here's where we document the possible routes; e.g., dc, recip, pythag, phi."})
    return response

