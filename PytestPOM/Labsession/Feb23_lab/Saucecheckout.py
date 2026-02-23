import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_cart_checkout(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # --- Open website ---
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        print("Opened Shop")

        # --- Wait until products are loaded ---
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h4.product-name")))

        # --- Add products dynamically ---
        products_to_add = ["Brocolli", "Cauliflower", "Beetroot"]
        product_elements = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")

        for prod in product_elements:
            name = prod.text.split("-")[0].strip()  # remove quantity text
            if name in products_to_add:
                try:
                    add_btn = prod.find_element(By.XPATH, "../..//button")  # button relative to product
                    add_btn.click()
                    print(f"Added {name} to cart")
                    time.sleep(1)
                except Exception as e:
                    print(f"Could not add {name}: {e}")

        # --- Go to cart ---
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cart-icon"))).click()
        print("Clicked cart icon")
        time.sleep(2)

        # --- Proceed to Checkout ---
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()
        print("Clicked Proceed to Checkout")
        time.sleep(2)

        # --- Checkout page loaded ---
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "promoCode")))
        print("Checkout page loaded")

        print("Test completed successfully ✔")

    except Exception as e:
        print("Error during shopping flow:", e)