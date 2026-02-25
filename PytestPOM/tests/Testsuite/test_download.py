import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

DOWNLOAD_DIR= "D:/Downloads"
class Test_download:
    def test_dw(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        flie_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(flie_path)
        time.sleep(2)
        driver.close()





