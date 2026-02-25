import time
import pytest
from Pages.Orange_page import  LoginPage
from Utilities.logger import get_logger
from Utilities.excel_utliss import get_excel_data

logger = get_logger()
test_data = get_excel_data("C:/Users/priya/PycharmProjects/Feb2026SeleniumPytestPom/testdata/login_data1.xlsx", "Sheet1")


class TestLogin:

    def test_valid_login(self, driver):
        logger.info("Opening  application")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        #create the object of login page
        lp=LoginPage(driver)
        logger.info("Entering the credentials")

        lp.login("Admin", "admin123")

        time.sleep(5)
        assert  "OrangeHRM" in driver.title

    def test_invalid_login(self, driver):
        logger.info("Opening  application")

        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        # create the object of login page
        lp = LoginPage(driver)
        logger.info("Entering the credentials")

        lp.login("Admin", "wrongpassword")
        time.sleep(5)

        assert "Invalid credentials" in lp.get_error_message()

    #test data stored in excel sheet
    @pytest.mark.parametrize("username,password", test_data)

    def test_login_excel(self, driver, username, password):
        logger.info("Opening  application")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        #create the object of login_page
        lp = LoginPage(driver)
        lp.login(username, password)

        if password == "admin123":
            assert "OrangeHRM" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()










