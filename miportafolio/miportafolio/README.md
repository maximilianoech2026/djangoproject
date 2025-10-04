Mi Portafolio Django

Este proyecto es un portafolio web desarrollado en Django, que incluye:

- Página de inicio con login.
- Lista de proyectos con calificación en estrellas.
- Gestión de usuarios mediante el sistema de autenticación de Django.
- Base de datos SQLite con proyectos predefinidos.

Estructura del proyecto:

miportafolio/
│
├─ manage.py
├─ db.sqlite3             # Base de datos con proyectos (opcional)
├─ miportafolio/          # Configuración del proyecto Django
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ proyectos/             # App principal
   ├─ models.py
   ├─ views.py
   ├─ admin.py
   ├─ templates/
   │  └─ proyectos/
   │     ├─ home.html
   │     ├─ lista.html
   │     └─ login.html
   └─ migrations/

Requisitos:

- Python 3.10 o superior
- Django 5.2.6
- Virtualenv (opcional)
- Navegador web moderno

Cómo ejecutar el proyecto:

1. Abrir la carpeta del proyecto en VS Code o terminal.

2. Crear un entorno virtual (opcional):

   python -m venv venv
   venv\Scripts\activate   # Windows
   # o
   source venv/bin/activate # Linux / Mac

3. Instalar Django:

   pip install django

4. Aplicar migraciones:

   python manage.py migrate

   > Si db.sqlite3 ya está incluida, este paso solo asegura que las migraciones estén al día.

5. Crear un superusuario (opcional):

   python manage.py createsuperuser

6. Ejecutar el servidor de desarrollo:

   python manage.py runserver

7. Abrir en el navegador:

   http://127.0.0.1:8000/

Login:

- Acceder con el usuario creado en `createsuperuser`.
- Al iniciar sesión, se redirige a la página de inicio con los proyectos.
- Para cerrar sesión, usar el botón “Cerrar sesión”.

Uso del proyecto:

- La página de inicio (home.html) muestra un saludo al usuario y un listado de proyectos con estrellas.
- La página de proyectos (lista.html) muestra todos los proyectos agregados en la base de datos.
- Los proyectos se cargan dinámicamente desde el modelo Proyecto usando SQLite.

Notas:

- Proyecto desarrollado para fines académicos.
- La base de datos está en SQLite, no requiere configuración adicional.
- Frontend simple con colores, listas y botones para mejorar la presentación.


Superusuario de desarrollo

- Usuario: maxha
- Contraseña: 1234
- Solo para pruebas locales y desarrollo.python manage.py runserver