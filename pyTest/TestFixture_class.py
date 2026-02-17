import pytest

@pytest.fixture()
def dbconnection():
    print("\n[Setup] Connecting to Database")
    yield
    print("\n[Teardown] Closing Database")

@pytest.mark.usefixtures("dbconnection")
class TestLogin:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("click on the Login button")

    def test_logout(self):
        print("user is logged out")
