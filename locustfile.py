from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        """
        Este método se ejecuta antes de que inicien las pruebas de carga para realizar cualquier configuración necesaria.
        """
        self.login_url = "/authenticate"
        self.secure_url = "/secure"

    @task
    def login_success(self):

        payload = {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
        }


        with self.client.post(self.login_url, data=payload, catch_response=True) as response:
            if response.status_code == 200:
                print("Inicio de sesión exitoso")


                with self.client.get(self.secure_url, catch_response=True) as secure_response:
                    if secure_response.status_code == 200:
                        print("Acceso a la página segura exitoso")
                        secure_response.success()
                    else:
                        print(f"Error al acceder a la página segura: {secure_response.status_code}")
                        secure_response.failure(f"No se pudo acceder a la página segura: {secure_response.status_code}")
            else:
                print(f"Error en el inicio de sesión exitoso: {response.status_code}")
                response.failure(f"Login fallido a pesar de credenciales correctas: {response.status_code}, {response.text}")

    @task
    def login_failure(self):

        payload = {
            "username": "incorrect_username",
            "password": "incorrect_password"
        }

        with self.client.post(self.login_url, data=payload, catch_response=True) as response:
            if "Your username is invalid!" in response.text or "invalid credentials" in response.text:
                print("Mensaje de error correcto mostrado")
                response.success()
            else:
                print(f"No se mostró el mensaje de error esperado: {response.status_code}, {response.text}")
                response.failure(f"Error en el manejo del login fallido: {response.status_code}, {response.text}")

    def on_stop(self):

        pass


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "https://the-internet.herokuapp.com"
