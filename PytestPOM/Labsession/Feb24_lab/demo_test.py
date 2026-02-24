from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_DemoWebShop:

    def test_complete_checkout_flow(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")

        wait = WebDriverWait(driver, 15)

        email = "ninja123@gmail.com"
        password = "Test@123"

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "Email"))).send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "input.button-1.login-button").click()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Books"))).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//input[@value='Add to cart'])[1]")
            )
        ).click()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping cart"))).click()

        wait.until(EC.element_to_be_clickable((By.ID, "termsofservice"))).click()
        driver.find_element(By.ID, "checkout").click()

        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input.button-1.new-address-next-step-button")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input.button-1.shipping-method-next-step-button")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable((By.ID, "paymentmethod_0"))
        ).click()

        driver.find_element(
            By.CSS_SELECTOR,
            "input.button-1.payment-method-next-step-button"
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input.button-1.payment-info-next-step-button")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input.button-1.confirm-order-next-step-button")
            )
        ).click()

        message = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.section.order-completed div.title strong")
            )
        ).text

        assert "Your order has been successfully processed!" in message

        print(" Order completed successfully!")

        driver.quit()