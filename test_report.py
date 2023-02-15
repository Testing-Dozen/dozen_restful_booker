import pytest
import requests

url_for_doc = "http://localhost:3005/report/swagger-ui/index.html"
url = "http://localhost:3005/report/"


def test_report_documentation():
    response = requests.get(url_for_doc)
    assert response.status_code == 200


def test_no_report_without_credentials():
    response = requests.get(url)
    assert response.status_code == 400