
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Keyboard:
    def test_Keyboard(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        # this is global setting that applies to every element location call for the entire session
        driver.implicitly_wait(2)

        #explicit wait
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, 2)
        wait.until(lambda _: radio_btn.is_displayed())

        #custom wait or fluent wait
        errors =[NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, 2, poll_frequency=.2,ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

        driver.close()



