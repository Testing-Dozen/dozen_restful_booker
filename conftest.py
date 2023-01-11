import pytest
import requests

local_env = "http://localhost:3002"
hosted_env = "http://automationintesting.online"

@pytest.fixture(scope= "function")
def branding_resp():
    local = False
    if local:
        r = requests.get(local_env + "/branding/")
    else:
        r = requests.get(hosted_env + "/branding/")
    yield r
    print ("This is where we write teardown - things to do after test")