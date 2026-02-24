import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_DragDrop:
    def test_dd(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        driver.maximize_window()

        time.sleep(4)

        actions = ActionChains(driver)
        source = driver.find_element(By.XPATH, "//div[@id='column-a']")
        dest = driver.find_element(By.XPATH, "//div[@id='column-b']")
        actions.drag_and_drop(source,dest)
        time.sleep(4)
        driver.close()

