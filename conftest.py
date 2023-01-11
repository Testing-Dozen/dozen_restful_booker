import pytest
import requests

local_env = "http://localhost:3002"

@pytest.fixture(scope= "class")
def local_address():
    x = requests.get(local_env + "/branding/")
    yield x
    print ("hello")