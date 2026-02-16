#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)


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




