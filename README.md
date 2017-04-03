Aplicacion desarrollada en Django para ser replicada en otros proyectos posteriores orientada a la informacion ambiental por consultoras.

Para levantar el servicio localmente:

python manage.py runserver 1234 (cualquier número de puerto disponible)

Si es primera vez o si se hizo modificaciones a los modelos o lo relacionado a la base de datos:

python manage.py migrate

Para ingresar a /admin, el usuario es "admin" y password "admin", en caso de no funcionar crear un super usuario con:

python manage.py createsuperuser
y escribir un user y password