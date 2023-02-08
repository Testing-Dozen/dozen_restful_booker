import pytest
import requests

#local_env = "http://localhost:3002"
local_env = "http://automationintesting.online"
hosted_env = "http://automationintesting.online"


@pytest.fixture(scope= "function")
def the_base_url():
    local = False
    print(local)
    url_to_use: str = ""
    if local:
        url_to_use = local_env
    elif not local:
        url_to_use = hosted_env
    yield local, url_to_use
    print("This is where we write teardown - things to do after test")


@pytest.fixture(scope="function")
def is_env_up(the_base_url):
    should_we = the_base_url[0]
    if not should_we:
        raise Exception("Environment is not up, we should not")
    address_to_use = the_base_url[1]
    yield should_we, address_to_use
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