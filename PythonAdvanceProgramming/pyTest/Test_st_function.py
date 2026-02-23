#function level set up and tear down
#these run before and run after each test function
import pytest


#set up at function level
def setup_function(function):
    print("Opening the browser")

#teardown up at function level
def teardown_function(function):
    print("Closing the browser")

# testcase1
@pytest.mark.sanity
def test_case1():
    print("Testcase1 is executed")

# testcase2

def test_case2():
    print("Testcase2 is executed")

# testcase3
def test_case3():
    print("Testcase3 is executed")




