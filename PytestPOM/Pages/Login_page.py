



from selenium.webdriver.common.by import By
class LoginPage:
    username_input = (By.NAME, 'username')
    password_input = (By.NAME, 'password')
    login_button = (By.XPATH, '//button[normalize-space()="Login"]')
    dashboard_text = (By.XPATH, '//div[normalize-space()="Dashboard"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)




