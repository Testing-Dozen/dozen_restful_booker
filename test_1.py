from approvaltests import verify, verify_as_json
import requests

def test_branding(is_env_up):
    assert is_env_up.status_code == 200
    #Verify the entire json with approvaltests
    verify_as_json(is_env_up.json())
    #Search for some string in the response text
    assert "Shady Meadows" in is_env_up.text
    #Search for specific value in specific place of json-structure
    assert is_env_up.json()["name"] == "Shady Meadows B&B"
    #Search deeper in structure and multiple items
    assert is_env_up.json()["map"]["latitude"] == 52.6351204 and is_env_up.json()["map"]["longitude"] == 1.2733774
    #Verify that there is a json structure present without caring about what is in it
    assert is_env_up.json()["description"]

def test_change_branding(admin):
    response = admin.put("http://localhost/branding/", json = "")
    assert response.status_code == 400

def test_change_branding_without_admin():
    response = requests.put("http://localhost/branding/", json = "")
    assert response.status_code == 400

import pytest

json1 = {
            "roomName": "999",
            "type": "Suite",
            "accessible": False,
            "description": "This is a lovely room",
            "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
            "roomPrice": "878",
            "features": [
                "WiFi",
                "TV"]}

json2 = {
            "roomName": "999",
            "type": "Suite",
            "accessible": True,
            "description": "This is a lovely room",
            "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
            "roomPrice": "878",
            "features": [
                "WiFi",
                "TV"]}

@pytest.mark.parametrize("variable", [json1, json2])
def test_create_room(admin, variable):
    response = admin.post("http://localhost/room/", json = variable)
    assert response.status_code == 201
    assert response.json()["roomName"] == "999"
    assert response.json()["description"] == "This is a lovely room"
    # verify_as_json(response.text)

def test_post_validation(admin):
    respone = admin.post("http://localhost/room/", json = "")
    assert respone.status_code == 400

def test_put_validation(admin):
    respone = admin.put("http://localhost/room/1", json = "")
    assert respone.status_code == 400

json3 = {
            "roomName": "777",
            "type": "Suite",
            "accessible": True,
            "description": "This is a lovely room",
            "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
            "roomPrice": "878",
            "features": [
                "WiFi",
                "TV"]}

def test_put(admin):
    respone = admin.put("http://localhost/room/1", json = json3)
    assert respone.ok

def test_get_rooms(admin):
    rooms = admin.get("http://localhost/room")
    verify_as_json(rooms.json())
