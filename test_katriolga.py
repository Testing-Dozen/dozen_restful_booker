import pytest
import requests

url = "http://localhost:3005/report/"

def test_katriolgareport ():
    response = requests.get (url)
    assert response.status_code == 400