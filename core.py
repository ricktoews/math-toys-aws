import json
import sys
sys.path.append('./modules')

from utils import normalize_event
from phi import phi_first_n
from dc import get_expansions, get_single_expansion
from phi import get_phi, get_phi_power
from pythag import get_pythag_by_corner

def handle_phi(response, path_parameters):
    up_to_power = path_parameters.get('up_to_power', '1')
    if up_to_power and up_to_power.isdigit():
        up_to_power = int(up_to_power)
        desc = f"Powers of Phi, up to power {up_to_power}"
        data = get_phi(int(up_to_power))
        response['body'] = json.dumps({"description": desc, "data": data})
    else:
        response['statusCode'] = 400
        response['body'] = json.dumps({"error": "Invalid power parameter"}) 
    return response

def handle_phi_power(response, path_parameters):
    power = path_parameters.get('power', '1')
    if power and power.isdigit():
        power = int(power)
        desc = f"Phi, raised to the power of {power}"
        data = get_phi_power(int(power))
        response['body'] = json.dumps({"description": desc, "data": data})
    else:
        response['statusCode'] = 400
        response['body'] = json.dumps({"error": "Invalid power parameter"}) 
    return response

def handle_dc(response, path_parameters):
    denom = path_parameters.get('denom', 1)
    if denom:
        denom = int(denom)
        desc = f"Decimal expansion for denominator {denom}"
        data = get_expansions(denom)
        response['body'] = json.dumps({"description": desc, "data": data})
    return response

def handle_recip(response, path_parameters):
    denom = path_parameters.get('denom', 1)
    if denom:
        denom = int(denom)
        desc = f"Decimal expansion for reciprocal of {denom}"
        data = get_single_expansion(1, denom)
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


def process_requests(event):
    normalized_event = normalize_event(event)

    path = normalized_event.get('path', '')
    path_parameters = normalized_event.get('pathParameters', {})
    response = {
        "statusCode": 200,
        "headers": {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*",  # Your domain
            "Access-Control-Allow-Methods": "GET, OPTIONS",  # Allow GET and preflight
            "Access-Control-Allow-Headers": "Content-Type"  # Basic headers
        }
    }
    desc = ''
    data = []

    route_handlers = {
        '/phi_power': handle_phi_power,
        '/phi': handle_phi,
        '/dc': handle_dc,
        '/recip': handle_recip,
        '/pythag': handle_pythag,
        '/': handle_root
    }

    for route, handler in route_handlers.items():
        if path.startswith(route):
            return handler(response, path_parameters)


