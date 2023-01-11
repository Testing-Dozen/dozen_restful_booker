from approvaltests import verify, verify_as_json

def test_branding(branding_resp):
    assert branding_resp.status_code == 200
    #Verify the entire json with approvaltests
    verify_as_json(branding_resp.json())
    #Search for some strong in the response text
    assert "Shady Meadows" in branding_resp.text
    #Search for specific value in specific place of json-structure
    assert branding_resp.json()["name"] == "Shady Meadows B&B"
    #Search deeper in structure and multiple items
    assert branding_resp.json()["map"]["latitude"] == 52.6351204 and branding_resp.json()["map"]["longitude"] == 1.2733774
    #Verify that there is a json structure present without caring about what is in it
    assert branding_resp.json()["description"]

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
