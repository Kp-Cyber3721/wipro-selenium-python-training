import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_WebTables:
    def test_webtables(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.maximize_window()

        rows = driver.find_elements(By.XPATH, "//table[@id= 'table1']/tbody/tr")
        for i in rows:
            print(i.text)
        time.sleep(2)

        cols = driver.find_elements(By.XPATH, "//table[@id= 'table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)
        time.sleep(2)

        celldata = driver.find_element(By.XPATH, "//table[@id= 'table1']/tbody/tr[3]/td[4]")
        assert "$100.00" in celldata.text

        driver.quit()