import pytest
import requests
import json

url = "http://localhost:3006/message/"

def test_message_api_creates_new_messages():
    response = requests.post(url, json={
        "description":"Hello, is there any discount?",
        "email":"jane@email.com",
        "name":"Jane",
        "phone":"12345678900",
        "subject":"Any discounts?"
    })
    assert response.status_code == 201

# Bug: Phonenumber-field accepts also letters.

def test_message_api_does_not_create_new_message_with_wrong_phonenumber():
    response = requests.post(url, json={
        "description":"Hello, is there any discount?",
        "email":"jane@email.com",
        "name":"Jane",
        "phone":"1234567jhgy",
        "subject":"Any discounts?"
    })
    assert response.status_code == 201
    assert "1234567jhgy" in response.text

# Bug: Email does not require "."

def test_message_api_creates_new_message_without_email_extension():
    response = requests.post(url, json={
        "description":"Hello, is there any discount?",
        "email":"jane@email",
        "name":"Jane",
        "phone":"12345678900",
        "subject":"Any discounts?"
    })
    assert response.status_code == 201

def test_message_api_does_not_create_messages_without_data():
    response = requests.post(url, json={})
    assert response.status_code == 400

def test_get_messages():
    response = requests.get(url)
    print(response.content)
    assert response.status_code == 200
# pytest .\test_message_svetlana.py::test_get_messages -s

def test_get_message_by_id():
    response = requests.get(url, params={"messageid":"1"})
    assert response.status_code == 200

def test_delete_message_by_id(admin):
    id = 9
    response = admin.delete(f"{url}{id}")
    assert response.status_code == 202
