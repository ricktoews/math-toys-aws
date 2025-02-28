import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# tests/test_core.py
from test_events import event
from core import process_requests

def test_reciprocal_7():
    response = process_requests(event.get('recip'))
    body = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert body["data"]["period"] == "142857"

def get_dc_14():
    response = process_requests(event.get('dc'))
    body = json.loads(response["body"])
    return body

def test_dc_2_14_repeating():
    body = get_dc_14()
    data = body.get("data")
    by_numerator = data.get("byNumerator")
    check_2_14 = by_numerator["2"]
    expansion_2_14 = check_2_14["expansion"]
    assert expansion_2_14 == "142857"

def scraps():
    check_1_14 = body["data"][0]
    check_2_14 = body["data"][1]
    print(f"====> test_dc_14 1/14", check_1_14)
    print(f"====> test_dc_14 2/14", check_2_14)
    non_repeating_1_14 = check_1_14["non_repeating"]
    repeating_1_14 = check_1_14["repeating"]
    period_length_1_14 = check_1_14["period_length"]
    period_1_14 = check_1_14["period"]
    non_repeating_2_14 = check_2_14["non_repeating"]
    repeating_2_14 = check_2_14["repeating"]
    period_length_2_14 = check_2_14["period_length"]

    assert response["statusCode"] == 200
    assert repeating_1_14 == 6
    assert repeating_2_14 == 6
    assert non_repeating_1_14 == 0
    assert non_repeating_2_14 == 1
    assert period_1_14 == "0714285"
    assert period_2_14 == "142857"

