import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Keyboard:
    def test_Keyboard(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        password = driver.find_element(By.XPATH, "//input[@name='pass']")
        seriesofaction = actions.move_to_element(email).click().key_down(Keys.SHIFT).send_keys("hello").key_up(
            Keys.SHIFT).key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).move_to_element(
            password).click().key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)

        seriesofaction.perform()



