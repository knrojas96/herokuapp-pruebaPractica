from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitHelper:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def wait_for_visibility(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"El elemento con localizador {locator} no fue visible dentro del tiempo especificado.")
            return None

    def wait_for_clickable(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"El elemento con localizador {locator} no fue clicable dentro del tiempo especificado.")
            return None

    def wait_for_element_present(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"El elemento con localizador {locator} no está presente en el DOM dentro del tiempo especificado.")
            return None


