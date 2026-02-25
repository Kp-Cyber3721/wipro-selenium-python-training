import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_window:

    def test_window(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        driver.implicitly_wait(10)
        clickhere=driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()
        time.sleep(10)
        #fetch the window handles of both tabs
        windows = driver.window_handles
        print(windows)
        # move the control to child window
        driver.switch_to.window(windows[1])

        # Get text from new window
        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text)
        time.sleep(2)
        driver.close()

        # get back to parent window
        driver.switch_to.window(driver.window_handles[0])
        clickhere.is_displayed()

        driver.quit()