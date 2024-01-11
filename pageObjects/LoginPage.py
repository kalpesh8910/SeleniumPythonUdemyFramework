from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "login-email")
    password = (By.ID, "login-password")
    LetsGoBtn = (By.XPATH, "//button[@type='submit']")

    def enterUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLoginButton(self):
        return self.driver.find_element(*LoginPage.LetsGoBtn)

