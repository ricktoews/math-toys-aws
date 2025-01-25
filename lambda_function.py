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
    
    if path.startswith('/phi'):
        power = path_parameters.get('power', 1)
        if power and power.isdigit():
            power = int(power)
            desc = f"phi to the power of {power}"
            data = get_phi(int(power))
            response['body'] = json.dumps({"description": desc, "data": data})
        else:
            response['statusCode'] = 400
            response['body'] = json.dumps({"error": "Invalid power parameter"}) 

    elif path.startswith('/dc'):
        denom = path_parameters.get('denom', 1)
        if denom:
            denom = int(denom)
            desc = f"decimal expansion for denominator {denom}"
            data = []
            for num in range(1, denom):
                data.append(calc_decimal(num, denom, 10))
            response['body'] = json.dumps({"description": desc, "data": data})

    elif path.startswith('/recip'):
        denom = path_parameters.get('denom', 1)
        if denom:
            denom = int(denom)
            desc = f"decimal expansion for reciprocal of {denom}"
            data = calc_decimal(1, denom, 10)
            response['body'] = json.dumps({"description": desc, "data": data})

    elif path.startswith('/pythag'):
        corner = path_parameters.get('corner', 1)
        if corner:
            corner = int(corner)
            desc = f"Pythagorean triples where c - b = {corner}"
            data = get_pythag_by_corner(corner)
            response['body'] = json.dumps({"description": desc, "data": data})

    else:
        response['statusCode'] = 404
        response['body'] = json.dumps({"error": "Invalid path"})

    # TODO implement
    return response
