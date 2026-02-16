# grouping -set of testcases run together - issue fix in that module
import pytest

def test_case1():
    print("Testcase1 is executed")

@pytest.mark.sanity
def test_case2():
    print("Testcase2 is executed")
@pytest.mark.regression
def test_case3():
    print("Testcase3 is executed")

def test_openbrowser():
    print("Opening the browser")











