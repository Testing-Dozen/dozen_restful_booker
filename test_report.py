import pytest
import requests

url = "http://localhost:3005/report/swagger-ui/index.html"

def test_report():
    response = requests.get(url)
    assert response.status_code == 200