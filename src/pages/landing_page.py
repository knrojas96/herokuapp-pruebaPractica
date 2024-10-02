from selenium.webdriver.common.by import By
from src.helpers.waitHelper import WaitHelper

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_helper = WaitHelper(driver)  # Crear instancia de Wait
        self.welcome_message = (By.XPATH, "//h4[text()='Welcome to the Secure Area. When you are done click logout below.']")
        self.flash_message = (By.ID, "flash")

    def is_welcome_message_displayed(self):
        welcome_msg = self.wait_helper.wait_for_visibility(self.welcome_message)
        return welcome_msg.is_displayed()

    def get_flash_message(self):
        flash_msg = self.wait_helper.wait_for_visibility(self.flash_message)
        return flash_msg.text