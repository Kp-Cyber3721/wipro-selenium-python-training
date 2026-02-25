from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_frame:

    def test_frame(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        frame=driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(frame)

        datepicker=driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()
        driver.close()
