
import pytest
from selenium import webdriver

from pages.upload_page import UploadPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_file_upload(setup):

    upload_page = UploadPage(setup)
    file_path = "/Users/krojas2/Downloads/Upload.png"

    upload_page.upload_file(file_path)

    confirmation_message = upload_page.get_confirmation_upload()  # Llamar al método correcto
    assert "File Uploaded!" in confirmation_message, "El archivo no se ha cargado correctamente."
