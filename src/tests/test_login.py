from threading import Thread
import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.landing_page import LandingPage
from env_variables import EnvVariables
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_success(setup):
    login_page = LoginPage(setup)
    landing_page = LandingPage(setup)

    login_page.enter_correct_credentials()
    login_page.click_login_button()

    assert landing_page.is_welcome_message_displayed()

    assert "You logged into a secure area!" in landing_page.get_flash_message()


def test_login_failure(setup):
    login_page = LoginPage(setup)

    login_page.enter_incorrect_credentials()
    login_page.click_login_button()

    # Verifica el mensaje de error
    assert "Your username is invalid!" in login_page.get_flash_message()


def test_landing_page_access_success(setup):
    login_page = LoginPage(setup)
    landing_page = LandingPage(setup)

    login_page.enter_correct_credentials()
    login_page.click_login_button()

    assert landing_page.is_welcome_message_displayed(), "This is where you can log into the secure area. Enter "



def test_landing_page_access_failure(setup):
    login_page = LoginPage(setup)
    landing_page = LandingPage(setup)

    login_page.enter_incorrect_credentials()
    login_page.click_login_button()
    landing_page.is_welcome_message_displayed()
