# Gendif-APIRESTful
APIRESTful de Perfiles de Usuario con Autenticación

## Características
- Autenticación mediante JWT y Cookies
- Conectado directamente al gestor de imágenes de Cloudinary

## Tecnologías Utilizadas
- Frameworks: Django y Django-Rest-Framework
- Gestor de imágenes: Cloudinary

## Instalación
```bash
git clone https://github.com/MauriiWhite/gendif-api.git
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```

## Antes de correr el servidor es necesario hacer lo siguiente:

Completa los siguientes campos al momento de haber realizado la instalación.
Dentro del archivo **.env** rellena:
```env
CLOUDINARY_CLOUD_NAME= *Tu nombre de Nube de Cloudinary*
CLOUDINARY_API_KEY= *Tu API KEY de Cloudinary*
CLOUDINARY_API_SECRET= *Tu APISECRET de Cloudinary*
```
Servicio de imágenes: [Cloudinary](https://cloudinary.com/)


En el del archivo **constants.py** dentro de la carpeta de **/api** completa lo siguiente:
```python
DEFAULT_PROFILE = ""
DEFAULT_PROFILE_URL = 
DEFAULT_SUBGROUP = ""
DEFAULT_SUBGROUP_URL = ""
DEFAULT_EVENT = ""
DEFAULT_EVENT_URL = ""
```
Todos los campos deben de ser de tipo **string**.

Un ejemplo de se su uso es el siguiente:
```python
DEFAULT_PROFILE = "default/picture.png"
DEFAULT_PROFILE_URL = "https://res.cloudinary.com/.../image/upload/.../default/picture.png"

DEFAULT_SUBGROUP = "default/subgroup.jpg"
DEFAULT_SUBGROUP_URL = "https://res.cloudinary.com/.../image/upload/.../default/subgroup.jpg"
```
Cabe destacar que debes de extraer la URL de tu imagen dentro del dashboard de Cloudinary y tener 3 archivos
de imágenes diferentes, tanto para profile, subgroup y event.

¡Enhorabuena!



