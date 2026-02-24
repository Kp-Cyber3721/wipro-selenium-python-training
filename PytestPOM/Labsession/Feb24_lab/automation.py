import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_AutomationPracticeFull:

    def test_automation_practice(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)
        actions = ActionChains(driver)

        auto_input = driver.find_element(By.ID, "autocomplete")
        auto_input.send_keys("Ind")
        time.sleep(1)
        suggestions = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/div")
        for suggestion in suggestions:
            if "India" in suggestion.text:
                suggestion.click()
                print(f"Autocomplete selected: {suggestion.text}")
                break

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        radio_btns = driver.find_elements(By.XPATH, "//input[@type='radio']")
        radio_btns[1].click()

        dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option2")

        driver.find_element(By.ID, "name").send_keys("Priya")
        driver.find_element(By.ID, "alertbtn").click()
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()

        driver.find_element(By.ID, "confirmbtn").click()
        confirm = driver.switch_to.alert
        print(f"Confirm text: {confirm.text}")
        confirm.dismiss()

        driver.find_element(By.ID, "openwindow").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print(f"New window title: {driver.title}")
        driver.close()
        driver.switch_to.window(windows[0])

        driver.find_element(By.ID, "opentab").click()
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        print(f"New tab title: {driver.title}")
        driver.close()
        driver.switch_to.window(tabs[0])

        hover_element = driver.find_element(By.ID, "mousehover")
        actions.move_to_element(hover_element).perform()
        print(" Hover performed")

        driver.switch_to.frame("courses-iframe")
        iframe_text_elements = driver.find_elements(By.XPATH, "//body//*")
        for elem in iframe_text_elements:
            if elem.text.strip() != "":
                print(elem.text.strip())
        driver.switch_to.default_content()

        rows = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")
        found = False
        for row in rows:
            if "Chennai" in row.text:
                found = True
                print(f"Chennai found in row: {row.text}")
                break

        skills_to_select = ["Advanced Selenium Framework", "PageObject", "TestNG", "Maven", "Jenkins", "C"]
        checkboxes = driver.find_elements(By.XPATH, "//table[@id='checkBoxOption']/tbody/tr/td/input")
        labels = driver.find_elements(By.XPATH, "//table[@id='checkBoxOption']/tbody/tr/td/label")
        for idx, label in enumerate(labels):
            if label.text.strip() in skills_to_select:
                checkboxes[idx].click()
                print(f"Selected: {label.text.strip()}")

        time.sleep(2)
        driver.quit()