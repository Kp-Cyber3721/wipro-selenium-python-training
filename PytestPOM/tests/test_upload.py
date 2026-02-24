import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Upload:
    def test_Upload(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys(r"D:\Downloads\project-assessment-report-23-02-2026.pdf")
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")

        upload.click()
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space() = 'File Uploaded!']")
        assert fileupload.text == "File Uploaded!"
        driver.close()





