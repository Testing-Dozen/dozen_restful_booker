import pytest
import requests

local_env = "http://localhost:3002"
hosted_env = "http://automationintesting.online"

@pytest.fixture(scope= "function")
def branding_resp() -> requests.Response:
    local = True
    if local:
        r = requests.get(local_env + "/branding/")
    else:
        r = requests.get(hosted_env + "/branding/")
    yield r
    print ("This is where we write teardown - things to do after test")

@pytest.fixture(scope= "session")
def admin() -> requests.Session:
    session = requests.Session()
    session.post("http://localhost:3004/auth/login", json=
    {"username": "admin", "password": "password"})
    print(session)
    yield session