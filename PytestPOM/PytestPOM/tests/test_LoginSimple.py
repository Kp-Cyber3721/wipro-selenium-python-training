import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)

# enter username
name = driver.find_element(By.NAME, "username")
name.send_keys("Admin")

# enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

time.sleep(4)

# click on login button
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()


