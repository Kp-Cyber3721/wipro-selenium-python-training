#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import sys

import pytest

@pytest.mark.xfail(reason="known bug in the third-Party library")
def test_function_with_bug():
    assert (1+1)==3 # this assertion will fail as excepted
# testcase1
@pytest.mark.sanity
def test_case1():
    print("Testcase1 is executed")

# testcase2
@pytest.mark.regression
def test_case2():
    print("Testcase2 is executed")

# testcase3
@pytest.mark.db
def test_case3():
    print("Testcase3 is executed")



#xfail with a condition

@pytest.mark.xfail(sys.platform == "win32" , reason ="Bug on windows")
def test():
    print("test on windows")

# this x fail will fail only on windows
#strict=True XFAIL FAILED fails the test duite
@pytest.mark.xfail(strict=True, reason ="bug #1234 is not fixed yet")
def test_function():
    assert True





