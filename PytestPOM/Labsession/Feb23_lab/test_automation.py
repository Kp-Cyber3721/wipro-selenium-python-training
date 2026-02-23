import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_add_to_cart_checkout(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    print(f"Logged in as {USERNAME}")
    time.sleep(2)

    items_to_add = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//button[contains(text(),'Add to cart')]")))
    for i, item in enumerate(items_to_add[:2]):
        item.click()
        print(f"Item {i+1} added to cart")
        time.sleep(1)

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    print("Navigated to cart")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    print("Clicked Checkout")
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    print("Checkout info filled")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    print("Order completed successfully")
    time.sleep(2)