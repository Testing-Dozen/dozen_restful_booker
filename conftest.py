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
    yield r, local
    print ("This is where we write teardown - things to do after test")

@pytest.fixture(scope="function")
def is_env_up(branding_resp):
    if not branding_resp[1]:
        raise Exception("Environment is not up")
    else:
        yield branding_resp[0]
'''
    with pytest.raises(Exception):
        if not branding_resp[0].status_code == 200:
            raise Exception("Environment is not up")
            '''
            
@pytest.fixture(scope= "session")
def admin() -> requests.Session:
    session = requests.Session()
    session.post("http://localhost:3004/auth/login", json=
    {"username": "admin", "password": "password"})
    print(session)
    yield session


from approvaltests import set_default_reporter
from approvaltests.reporters import DiffReporter, quiet_reporter

@pytest.fixture(scope="session", autouse=True)
def reporter():
    #set_default_reporter(DiffReporter())
    set_default_reporter(quiet_reporter)



'''
def if_something():
    """As a string the check is available for pytest before test run"""
    return ‘”automationintesting.online in config.getoption("base_url")'
    '''