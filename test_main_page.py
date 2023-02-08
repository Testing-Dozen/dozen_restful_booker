import pytest
import requests

url = "https://automationintesting.online"

def test_main_page():
    response = requests.get(url)
    assert response.status_code == 200