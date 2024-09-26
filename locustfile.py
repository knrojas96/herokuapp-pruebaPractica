from lib2to3.pgen2 import driver

from jinja2 import environment
from locust import HttpUser, TaskSet, task, between
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.landing_page import LandingPage
from src.env_variables import EnvVariables
from dotenv import load_dotenv


user_count = 0
max_users = 200
class UserBehavior(TaskSet):

    def on_start(self):
        """Se ejecuta al inicio de la prueba de carga"""
        self.driver = webdriver.Chrome()
        self.driver.get(EnvVariables.get_herokuapp_login())
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.landing_page = LandingPage(self.driver)

    @task
    def login_success(self):
        self.login_page.enter_correct_credentials()
        self.login_page.click_login_button()

        assert self.landing_page.is_welcome_message_displayed(), "El mensaje de bienvenida no fue encontrado."
        print("Inicio de sesión exitoso")

    @task
    def login_failure(self):

        self.login_page.enter_incorrect_credentials()
        self.login_page.click_login_button()

        assert "Your username is invalid!" in self.login_page.get_flash_message(), "El mensaje de error no fue encontrado."
        print("Inicio de sesión fallido")


    @task
    def login_failure(self):

        self.login_page.enter_incorrect_credentials()
        self.login_page.click_login_button()



def on_stop(self):
    if self.driver:
        self.driver.quit()


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "https://the-internet.herokuapp.com/login"
