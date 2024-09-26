# Proyecto de Pruebas Automatizadas con Selenium y python
 proyecto automatización casos de prueba de login utilizando Selenium WebDriver en Python, aplicando el patrón de diseño Page Object Model POM.

## Requisitos

1. Python 3.8+
2. Google Chrome (última versión)
3. Chromedriver compatible con la versión de Chrome

## Instalación

1. Clona este repositorio:
   
   git clone [xxxxx]

## Configuración de Variables de Entorno

Este taller utiliza variables sensibles (credenciales) que no deben subirse al repositorio.Se colocaron las credenciales independientes del codigo .env sin embargo por temas del ejercicio y la facilidad en la revisión se deja archivo en github y no se incluye en gitignore:

asegurate de tener instalado
pip install python-dotenv ó pip3 install python-dotenv (dependiendo la version de python)

## Cargue del archivo

Finalmente en la clase "test_upload" reemplazar la ruta donde esta almacenado el archivo a cargar , es importante garantizar que se encuentre en su PC local al momento de la ejecución.
file_path = "/Users/krojas2/Downloads/Upload.png"
