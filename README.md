# Espacios Comunitarios API

Este proyecto es una API REST desarrollada con **Django** y **Django Rest Framework** para la gestión de una base de datos de Espacios Comunitarios que asisten a la población en situación de vulnerabilidad. La API provee información sobre estos espacios, la asistencia brindada a cada uno de ellos y sobre los referentes de cada espacio.

---

## 🚀 Tecnologías utilizadas
- **Django**
- **Django Rest Framework**
- **JWT (JSON Web Tokens)** para autenticación
- **SQLite** para la gestión de la base de datos

---

## 📌 Instalación
1. Clonar el repositorio:
```bash
 git clone https://github.com/GonAlvarado/api_espacios_comunitarios.git
```
2. Crear un entorno virtual y activarlo:
```bash
python -m venv env
source env/bin/activate  # En Windows usa: .\env\Scripts\activate
```
3. Instalar las dependencias requeridas:
```bash
pip install -r requirements.txt
```
4. Realizar migraciones para configurar la base de datos:
```bash
python manage.py migrate
```
5. Crear un superusuario para acceder al panel de administración de Django:
```bash
python manage.py createsuperuser
```
6. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

---

## 📖 Uso
La API ofrece diferentes endpoints para gestionar los espacios comunitarios, la asistencia brindada y los referentes.

### 🔑 Autenticación
El sistema utiliza autenticación basada en tokens **JWT**. Para obtener un token, se debe enviar una solicitud **POST** con las credenciales de usuario al endpoint correspondiente.

### 🌐 Endpoints principales
- `/api/login/`: Autenticación.
- `/api/espacios/`: Gestión de Espacios Comunitarios.
- `/api/referentes/`: Gestión de referentes.

---

## 📄 Licencia
Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## 📬 Contacto
Cualquier consulta o sugerencia puede ser enviada a: gonalvarado86@gmail.com.

