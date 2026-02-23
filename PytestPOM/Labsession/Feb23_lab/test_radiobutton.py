import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
radio2.click()

print("Radio2 Selected:", radio2.is_selected())

time.sleep(2)

checkbox1 = driver.find_element(By.XPATH, "//input[@value='option1']")
checkbox1.click()

checkbox3 = driver.find_element(By.XPATH, "//input[@value='option3']")
checkbox3.click()

print("Option1 Selected:", checkbox1.is_selected())
print("Option3 Selected:", checkbox3.is_selected())

time.sleep(3)
driver.close()