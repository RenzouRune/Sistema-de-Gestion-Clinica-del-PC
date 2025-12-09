# Sistema de Gestión Clínica del PC

Aplicación web desarrollada con Django para gestionar recepción, diagnóstico y entrega de equipos informáticos en una clínica técnica. 
Facilita la administración de usuarios, asignación de tareas a estudiantes y seguimiento de reportes.

---

## Índice
- [Características Principales](#características-principales)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Uso](#uso)
- [API](#api)

---

## Características Principales

- **Gestión de Usuarios y Roles**: Sistema de autenticación con roles personalizados para administradores, estudiantes y personal de la clínica.
- **Recepción de Equipos**: Registro de equipos informáticos recibidos de clientes, incluyendo detalles del cliente, tipo de equipo y descripción del problema.
- **Asignación de Diagnósticos**: Asignación automática o manual de equipos a estudiantes para su diagnóstico y reparación.
- **Seguimiento de Evaluaciones**: Registro de evaluaciones realizadas por los estudiantes, con calificaciones y observaciones.
- **Gestión de Entregas**: Control de reportes de diagnóstico y estado de entrega de equipos reparados a los clientes.
- **Interfaz Web Intuitiva**: Plantillas HTML responsivas para una experiencia de usuario fluida en todas las operaciones.

---

## Tecnologías Utilizadas

- **Backend**: Django 5.2.6  
- **Base de Datos**: PostgreSQL (configurable para otros RDBMS)  
- **API**: Django REST Framework 3.16.1  
- **Otros**: python-dotenv para variables de entorno, psycopg2-binary para conexión a PostgreSQL  

---

## Requisitos Previos

- Python 3.11+  
- PostgreSQL  
- Git  

---

## Instalación y Configuración

1. Clonar el repositorio:

```bash
git clone https://github.com/RenzouRune/Sistema-de-Gestion-Clinica-del-PC.git

cd Sistema-de-Gestion-Clinica-del-PC
```

2. Crear un archivo '.env' en la raíz del proyecto:

```py
DB_NAME="nombre_base_datos"
DB_USER="usuario"
DB_PASSWORD="contraseña"
DB_HOST="localhost"
DB_PORT="5432"
```
* Este proyecto se trabajó utilizando PostgreSQL. Si quieres usar otro RDBMS, modifica 'ENGINE' en Clinica_PC/settings.py.

```python
#settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',    #Modificar esto
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

3. Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv

source venv/bin/activate      #Linux/Mac
venv\Scripts\activate         #Windows

pip install -r requirements.txt
```

4. Migrar base de datos:

```bash
python manage.py migrate
```

5. Crear superusuario:

```bash
python manage.py createsuperuser
```

6. Ejecutar servidor:

```bash
python manage.py runserver
```

---

## Uso

1. Accede a la aplicación en tu navegador (por defecto: http://127.0.0.1:8000/)  

2. Inicia sesión con tus credenciales  

3. Navega por la aplicación web e interactúa con ella:  

   - **Recepción**:  
     - Gestión de equipos (registro de nuevos ingresos)  

   - **Diagnóstico**:  
     - Gestión de alumnos  
     - Gestión de asignación alumno-equipo  
     - Gestión de diagnósticos y soluciones  

   - **Entrega**:  
     - Gestión de reportes  
     - Control de estado y entrega de equipos reparados a los clientes  

---

## API

El sistema expone un conjunto de endpoints REST para gestionar los equipos en la clínica.  
Todos los endpoints están bajo el prefijo `/recepcion/api/recepcion/`.

### Endpoints disponibles

| Método | Endpoint                                   | Descripción                                |
|--------|--------------------------------------------|--------------------------------------------|
| GET    | `/recepcion/api/recepcion/`                | Obtiene el listado de equipos registrados. |
| POST   | `/recepcion/api/recepcion/registrar/`      | Registra un nuevo equipo.                  |
| PUT    | `/recepcion/api/recepcion/modificar/<pk>/` | Modifica la información de un equipo.      |
| DELETE | `/recepcion/api/recepcion/eliminar/<pk>/`  | Elimina un equipo por su ID.               |

### Ejemplos de uso en Postman

- **Obtener listado de equipos**

método  = GET 
url     = http://127.0.0.1:8000/recepcion/api/recepcion/
Headers = Accept: application/json
Body    = (no aplica)

- **Registrar un nuevo equipo**

Método  = POST 
Url     = http://127.0.0.1:8000/recepcion/api/recepcion/registrar/ 
Headers = Content-Type: application/json
Body    =
```Json
{
    "cliente":"Pedro",
    "tipo":"PC",
    "problema":"No enciende",
}
```

- **Modificar un equipo existente**

Metodo   = PUT
Url      = http://127.0.0.1:8000/recepcion/api/recepcion/modificar/1/
Headers  = Content-Type: application/json
           Accept: application/json
Body     =
```Json
{
  "cliente": "Pedro",
  "tipo": "PC",
  "problema": "Batería no funciona"
}
```

- **Eliminar un equipo**

Método  = DELETE 
Url     = http://127.0.0.1:8000/recepcion/api/recepcion/eliminar/1/
Headers = Accept: application/json
Body    = (vacío)

* Notas:
     - Las respuestas se entregan en formato JSON.
     - Los códigos de estado HTTP siguen el estándar:
         -200 OK           → Operación exitosa
         -201 Created      → Registro creado
         -400 Bad Request  → Error en los datos enviados
         -404 Not Found    → Equipo no encontrado