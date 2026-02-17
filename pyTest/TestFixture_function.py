

import pytest
def openbrowser():
    print("Opening browser")
@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user is logged out")

#class level

@pytest.fixture(scope="class")
def openbrowser():
    print("\n[Setup] Opening browser for class")
    yield
    print("\n[Teardown] Closing browser for class")
class TestLogin:
    def test_login(self, openbrowser):
        print("Test Login")
    def test_logout(self, openbrowser):
        print("Test Logout")

#module level

@pytest.fixture(scope="module")
def setup_module():
    print("\n[Setup] Module-level setup")
    yield
    print("\n[Teardown] Module-level teardown")

def test_one(setup_module):
    print("Test One")

def test_two(setup_module):
    print("Test Two")







