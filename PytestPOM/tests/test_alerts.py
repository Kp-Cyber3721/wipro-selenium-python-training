import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_JSAlerts:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_js_alerts(self, driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)

        simple_alert_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        simple_alert_btn.click()
        alert = driver.switch_to.alert
        print("Simple Alert Text:", alert.text)
        time.sleep(5)
        alert.accept()
        print("Simple Alert accepted")
        time.sleep(2)

        confirm_alert_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confirm_alert_btn.click()
        alert = driver.switch_to.alert
        print("Confirmation Alert Text:", alert.text)
        time.sleep(5)
        alert.dismiss()
        print("Confirmation Alert dismissed")
        time.sleep(2)

        prompt_alert_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        prompt_alert_btn.click()
        alert = driver.switch_to.alert
        print("Prompt Alert Text:", alert.text)
        time.sleep(5)
        alert.send_keys("Test Hello")
        alert.accept()
        print("Prompt Alert accepted with text 'Test Hello'")
        time.sleep(2)

        result = driver.find_element(By.ID, "result").text
        print("Result on page:", result)