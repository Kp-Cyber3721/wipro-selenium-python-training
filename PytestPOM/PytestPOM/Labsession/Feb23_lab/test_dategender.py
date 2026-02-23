import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)

male_radio = driver.find_element(By.XPATH, "//input[@id='male']")
male_radio.click()

print("Male Selected:", male_radio.is_selected())

time.sleep(2)

monday_checkbox = driver.find_element(By.XPATH, "//input[@id='monday']")
monday_checkbox.click()

sunday_checkbox = driver.find_element(By.XPATH, "//input[@id='sunday']")
sunday_checkbox.click()

print("Monday Selected:", monday_checkbox.is_selected())
print("Sunday Selected:", sunday_checkbox.is_selected())

time.sleep(3)
driver.quit()