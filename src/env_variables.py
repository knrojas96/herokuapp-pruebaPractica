
# env_variables.py
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

class EnvVariables:
    @staticmethod
    def get_username():
        return os.getenv('CORRECT_USERNAME')

    @staticmethod
    def get_password():
        return os.getenv('CORRECT_PASSWORD')

    @staticmethod
    def get_incorrect_username():
        return os.getenv('INCORRECT_USERNAME')

    @staticmethod
    def get_incorrect_password():
        return os.getenv('INCORRECT_PASSWORD')

    @staticmethod
    def get_herokuapp_login():
        return os.getenv('HEROKUAPP_LOGIN_URL', 'https://the-internet.herokuapp.com/login')

