from approvaltests import verify_as_json
import requests

def test_branding(branding_resp):
    assert branding_resp.status_code == 200
    #Verify the entire json with approvaltests
    verify_as_json(branding_resp.json())
    #Search for some string in the response text
    assert "Shady Meadows" in branding_resp.text
    #Search for specific value in specific place of json-structure
    assert branding_resp.json()["name"] == "Shady Meadows B&B"
    #Search deeper in structure and multiple items
    assert branding_resp.json()["map"]["latitude"] == 52.6351204 and branding_resp.json()["map"]["longitude"] == 1.2733774
    #Verify that there is a json structure present without caring about what is in it
    assert branding_resp.json()["description"]

def test_change_branding(admin):
    response = admin.put("http://localhost/branding/", json = "")
    assert response.status_code == 400

def test_change_branding_without_admin():
    response = requests.put("http://localhost/branding/", json = "")
    assert response.status_code == 400