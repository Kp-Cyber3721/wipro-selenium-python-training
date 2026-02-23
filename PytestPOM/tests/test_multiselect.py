import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_single_and_multi_option(driver):
    driver.get("https://trytestingthis.netlify.app/")
    wait = WebDriverWait(driver, 10)

    # --- Single-select dropdown ---
    single_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "option"))))
    single_dropdown.select_by_visible_text("Option 1")
    print("Single-select chosen: Option 1")
    time.sleep(2)  # wait after step

    # --- Multi-select checkboxes ---
    multi_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))

    # Select first and third checkboxes
    multi_options[0].click()
    print("Multi-select chosen: Option 1")
    time.sleep(2)  # wait after step

    multi_options[2].click()
    print("Multi-select chosen: Option 3")
    time.sleep(2)  # wait after step

    # --- Assertions ---
    assert single_dropdown.first_selected_option.text == "Option 1"
    assert multi_options[0].is_selected()
    assert multi_options[2].is_selected()
    print("All selections verified!")