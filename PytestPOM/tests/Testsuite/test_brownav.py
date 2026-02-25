import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_link:
    def test_link(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://trytestingthis.netlify.app/")
        driver.maximize_window()
        time.sleep(2)

        title =driver.title
        print(title)

        url = driver.current_url
        print(url)

        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.refresh()
        driver.quit()







