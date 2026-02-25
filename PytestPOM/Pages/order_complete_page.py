from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderCompletePage:
    success_message = (By.XPATH,"//h2[@class='complete-header']")

    def __init__(self, driver):
        self.driver = driver

    def get_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message))
        return self.driver.find_element(*self.success_message).text