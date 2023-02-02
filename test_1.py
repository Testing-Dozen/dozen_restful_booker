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



def test_create_room(admin):
    response = admin.post("http://localhost/room/", json={
            "roomName": "999",
            "type": "Suite",
            "accessible": False,
            "description": "This is a lovely room",
            "image": "https://www.mwtestconsultancy.co.uk/img/room1.jpg",
            "roomPrice": "878",
            "features": [
                "WiFi",
                "TV"]})
    assert response.status_code == 201
    verify_as_json(response.text)

def test_get_rooms(admin):
    rooms = admin.get("http://localhost/room")
    verify_as_json(rooms.json())
