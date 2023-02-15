import requests

json4 = {"bookingdates":{"checkin":"","checkout":""},"depositpaid":False,"firstname":"","lastname":"","roomid":1,"email":"","phone":""}

def test_booking_empty_fields():
    response = requests.post("http://localhost/booking/", json = json4)
    assert response.status_code == 400