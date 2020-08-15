from nose.tools import assert_true
import requests
import json

headers = {
    'X-Auth-Token': 'e051043b86624518a57a263f9388d198'
}


def test_validate_200():
    response = requests.get('https://api.football-data.org/v2/teams/12', headers=headers)
    assert_true(response.status_code == 200)

def test_validate_403():
    response = requests.get('https://api.football-data.org/v2/teams/12')
    assert_true(response.status_code == 403)

def test_more_than_20_squad_members():
    response = requests.get('https://api.football-data.org/v2/teams/12', headers=headers)
    data = json.loads(response.content)
    assert_true(len(data["squad"]) > 20)

