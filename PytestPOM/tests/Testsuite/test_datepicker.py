import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_datepicker():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rsuitejs.com/components/date-picker/")
    time.sleep(3)

    basic = driver.find_element(By.XPATH, "//span[text()='Basic']")
    driver.execute_script("arguments[0].scrollIntoView();", basic)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='MM/dd/yyyy']").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//span[text()='24']").click()

    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='OK']").click()

    time.sleep(3)

    driver.quit()






