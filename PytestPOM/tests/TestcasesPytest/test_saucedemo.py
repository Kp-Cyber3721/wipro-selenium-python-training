import time

import pytest
from Utilities.excel_utils import get_excel_data
from Utilities.logger import get_logger
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.order_complete_page import OrderCompletePage

logger = get_logger()

excel_path = r"C:\Users\priya\PycharmProjects\Feb2026SeleniumPytestPom\testdata\login_data.xlsx"

test_data = get_excel_data(excel_path, "Sheet1")

class TestSauceDemo:

    @pytest.mark.parametrize("username,password,first_name,last_name,postal_code", test_data)
    def test_login_using_excel(self, driver, username, password, first_name, last_name, postal_code):
        logger.info(f"Launching SauceDemo with user: {username}")

        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login(username, password)
        time.sleep(4)

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.go_to_cart()

        time.sleep(4)
        cart = CartPage(driver)
        cart.click_checkout()

        time.sleep(4)
        checkout = CheckoutPage(driver)
        checkout.enter_checkout_info(first_name, last_name, postal_code)
        time.sleep(4)
        checkout.click_continue()
        checkout.click_finish()

        time.sleep(4)
        complete = OrderCompletePage(driver)
        assert "Thank you" in complete.get_success_message()