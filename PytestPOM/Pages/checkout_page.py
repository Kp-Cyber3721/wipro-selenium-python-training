from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_button = (By.XPATH, "//input[@id='continue']")
    finish_button = (By.XPATH, "//button[@id='finish']")

    def __init__(self, driver):
        self.driver = driver

    def enter_checkout_info(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()

    def click_finish(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.finish_button)).click()