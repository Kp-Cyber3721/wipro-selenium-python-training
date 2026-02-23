#fixture are the piece of code which are run before the testcases or after the testcases
import pytest
from Test_SimpleFixture import api_url
def test_case1():
    print("Testcase1 is executed")

@pytest.mark.sanity
def test_case2():
    print("Testcase2 is executed")
@pytest.mark.regression
def test_case3():
    print("Testcase3 is executed")

def test_case4():
    print("Testcase4 is executed")

def test_case5():
    print("Testcase5 is executed")

def test_login():
    print("Login test is executed")

def test_api(api_url):
    assert  "https" in api_url








