import pytest
@pytest.fixture(params=["chrome","firefox"])
#request - pytest object that contains information about who is calling the fixture and with what data

def browser(request):
    print("current browser:", request.param)
    return request.param

def testbrowser(browser):
    assert browser in ["chrome","firefox"]



@pytest.mark.parametrize("number,expected", [
    (2, "even"),
    (3, "odd"),
    (10, "even"),
    (15, "odd")
])
def test_even_odd(number, expected):
    assert (number % 2 == 0 and expected == "even") or \
           (number % 2 != 0 and expected == "odd")





