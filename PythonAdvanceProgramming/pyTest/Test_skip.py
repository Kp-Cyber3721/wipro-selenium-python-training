#skip - if defects are there
#skip - if the testcases are absolute
#windows , mobile -OS dependency
#browsers - FF ,IE , Chrome

import pytest

def test_case1():
    print("Testcase1 is executed")
@pytest.mark.skip
def test_case2():
    print("Testcase2 is executed")

def test_case3():
    print("Testcase3 is executed")



def test_openbrowser():
    print("Opening the browser")






