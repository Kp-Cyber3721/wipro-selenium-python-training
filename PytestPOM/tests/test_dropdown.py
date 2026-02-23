import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

dropdown = driver.find_element(By.ID, "dropdown-class-example")
sel = Select(dropdown)

sel.select_by_visible_text("Option1")
time.sleep(2)
sel.select_by_value("option2")
time.sleep(2)
sel.select_by_index(3)
time.sleep(2)

driver.quit()