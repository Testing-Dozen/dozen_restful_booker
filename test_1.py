import requests
from approvaltests import verify

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