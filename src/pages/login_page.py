from selenium.webdriver.common.by import By
from src.helpers.waitHelper import WaitHelper
from src.env_variables import EnvVariables

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)  # Instancia WaitHelper para manejar las esperas
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.CSS_SELECTOR, ".flash")
        self.logout_button = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def enter_correct_credentials(self):
        username = EnvVariables.get_username()
        password = EnvVariables.get_password()

        username_input = self.wait.wait_for_visibility(self.username_field)
        username_input.send_keys(username)

        password_input = self.wait.wait_for_visibility(self.password_field)
        password_input.send_keys(password)

    def enter_incorrect_credentials(self):
        username = EnvVariables.get_incorrect_username()
        password = EnvVariables.get_incorrect_password()

        username_input = self.wait.wait_for_visibility(self.username_field)
        username_input.clear()  # Limpia el campo si es necesario
        username_input.send_keys(username)

        password_input = self.wait.wait_for_visibility(self.password_field)
        password_input.send_keys(password)

    def click_login_button(self):
        login_btn = self.wait.wait_for_clickable(self.login_button)
        login_btn.click()

    def click_logout_button(self):
        logout_btn = self.wait.wait_for_clickable(self.logout_button)
        logout_btn.click()

    def get_flash_message(self):
        flash = self.wait.wait_for_visibility(self.flash_message)
        return flash.text
