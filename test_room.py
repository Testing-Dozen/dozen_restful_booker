from approvaltests import verify, verify_as_json
import requests
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
    response = admin.post("http://localhost/room/", json = "")
    assert response.status_code == 400

def test_put_validation(admin):
    response = admin.put("http://localhost/room/1", json = "")
    assert response.status_code == 400

json3 = {
            "roomName": "666",
            "type": "Suite",
            "accessible": True,
            "description": "This is a lovely room",
            "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
            "roomPrice": "878",
            "features": [
                "WiFi",
                "TV"]}

def test_put(admin):
    response = admin.put("http://localhost/room/1", json = json3)
    assert response.ok

@pytest.mark.xfail
def test_get_rooms(admin):
    rooms = admin.get("http://localhost/room")
    verify_as_json(rooms.json())


