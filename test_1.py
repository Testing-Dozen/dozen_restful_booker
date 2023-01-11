import requests
from approvaltests import verify, verify_as_json

def test_post_auth_token():
    '''This one starts with getting the response, but then processes the
    response further to get to just the token part by slicing the string.
    There are other ways of doing this too.

    In addition, authenticated login is only needed for the admin functionalities.
    So we won't need this before testing the admin functions.'''
    token = requests.post("http://localhost:8080/auth/login", json=
    {"username": "admin", "password": "password"}).headers['Set-Cookie'].split(';')[0].split('=')[1]
    verify(token)
    # {'Set-Cookie': 'token=78Jki9cmDPjBfKjv; Path=/', 'Date': 'Wed, 04 Jan 2023 17:47:25 GMT', 'Keep-Alive': 'timeout=60', 'Connection': 'keep-alive, keep-alive', 'Content-Length': '0'}

def test_branding(local_address):
    assert local_address.status_code == 200
    verify_as_json(local_address.json())
    assert "Shady Meadows" in local_address.text
    assert local_address.json()["name"] == "Shady Meadows B&B"
    assert local_address.json()["map"]["latitude"] == 52.6351204
    assert local_address.json()["map"]["longitude"] == 1.2733774
    assert local_address.json()["description"]

def test_branding_2():
    response = requests.get("http://automationintesting.online/branding/")
    assert response.status_code == 200
    verify(response.text)
    assert "Shady Meadows" in response.text
    assert response.json()["name"] == "Shady Meadows B&B"
    assert response.json()["map"]["latitude"] == 52.6351204
    assert response.json()["map"]["longitude"] == 1.2733774
    assert response.json()["description"]
