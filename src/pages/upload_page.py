import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UploadPage:
    def __init__(self, driver):
        self.driver = driver
        self.file_input = (By.ID, "file-upload")
        self.submit_button = (By.ID, "file-submit")
        self.confirmation_message = (By.XPATH, "//h3[contains(text(),'File Uploaded!')]")


    def upload_file(self, file_path):
        self.driver.find_element(*self.file_input).send_keys(file_path)
        self.driver.find_element(*self.submit_button).click()

    def get_confirmation_upload(self):
        wait = WebDriverWait(self.driver, 10)
        message = wait.until(EC.presence_of_element_located(self.confirmation_message))
        return message.text
