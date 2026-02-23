# used inside the class
# it will run for every class definition 0nce  it will run starting and  at ending of the class


class Testclass1:
    #class level set up

    def setup_class(cls):
        print("API Authorization needed with username and password")
    def teardown_class(cls):
        print("API Authorization closed")

    def setup_method(method):
        print("Opening the browser")

    # teardown up at function level
    def teardown_method(method):
        print("Closing the browser")

    # testcase1
    def test_case1(self):
        print("Testcase1 is executed")

    # testcase2
    def test_case2(self):
        print("Testcase2 is executed")

    # testcase3
    def test_case3(self):
        print("Testcase3 is executed")

class Testclass2:
    # testcase1
    def test_case1(self):
        print("Testcase1 is executed")

    # testcase2
    def test_case2(self):
        print("Testcase2 is executed")

    # testcase3
    def test_case3(self):
        print("Testcase3 is executed")










