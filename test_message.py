import pytest
import requests
import json

url = "https://automationintesting.online/message/"


def test_message_api_creats_new_messages():
    response = requests.post(url, json={
        'description': 'Hello, is there any discounts?',
        'email': 'jane@email.com',
        'name': 'Jane',
        'phone': '12345678900',
        'subject': 'Any discounts?',
    })
    assert response.status_code == 201
    print(response.text)


def test_message_sergei_and_mii(base_url):
    load = {"name": "", "email": "", "phone": "", "subject": "", "description": "hi, how are you"}
    response = requests.post(f"{base_url}/message/", json=load)
    assert response.status_code == 400


def test_message_sergei_and_mii_2(base_url):
    load = {"messageid": 2, "name": "Jay Jay Jay Jay ", "email": "jeejee@example.com", "phone": "+12883456789",
            "subject": "important",
            "description": "Hello World, this is us "}
    response = requests.post(f"{base_url}/message/", json=load)
    print(response.content)
    assert response.ok
    assert response.json()["messageid"] is not 2
