import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver_path = os.path.abspath("drivers/chromedriver.exe")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


def close_ads(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@id,'google')]"))
        )
        driver.switch_to.default_content()
    except:
        pass


# Test 1 : Register
def test_register_user(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]"))
    ).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "name"))
    ).send_keys("TestUser")

    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("newuser12345678@gmail.com")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']"))
    )


# Test 2 : Valid Login
def test_login_valid(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]"))
    ).click()

    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("newuser1234567@gmail.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("1234567")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )


# Test 3 : Invalid Login
def test_login_invalid(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()

    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("wrong@gmail.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("wrong")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'incorrect')]"))
    )


# Test 4 : Products
def test_all_products(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]"))
    )


# Test 5 : Search
def test_search_product(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    ).send_keys("Dress")

    driver.find_element(By.ID, "submit_search").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Searched Products')]"))
    )


# Test 6 : Contact
def test_contact_us(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.find_element(By.XPATH, "//a[contains(text(),'Contact us')]").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    ).send_keys("Test User")

    driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
    driver.find_element(By.NAME, "subject").send_keys("Automation Test")
    driver.find_element(By.ID, "message").send_keys("Testing contact form")

    driver.find_element(By.NAME, "submit").click()


# Test 7 : Subscription
def test_subscription(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "susbscribe_email"))
    ).send_keys("subscribe@gmail.com")

    driver.find_element(By.ID, "subscribe").click()

def test_product_detail_page(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]"))
    )

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'View Product')])[1]"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='product-information']"))
    )

    assert driver.find_element(By.XPATH, "//h2").is_displayed()  # product name
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Category')]").is_displayed()
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Rs.')]").is_displayed()
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Availability')]").is_displayed()
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Condition')]").is_displayed()
    assert driver.find_element(By.XPATH, "//*[contains(text(),'Brand')]").is_displayed()

def test_search_product_verified(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    ).send_keys("Dress")

    driver.find_element(By.ID, "submit_search").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Searched Products')]"))
    )

    results = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']")
    assert len(results) > 0

def test_verify_subscription_home(driver):
    driver.get("https://automationexercise.com")
    close_ads(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Subscription')]"))
    )

    driver.find_element(By.ID, "susbscribe_email").send_keys("testsubscribe@gmail.com")
    driver.find_element(By.ID, "subscribe").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'successfully subscribed')]"))
    )


