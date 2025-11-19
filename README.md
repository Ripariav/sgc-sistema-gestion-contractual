# SGC - Sistema de Gestión Contractual

## Descripción

El **SGC - Sistema de Gestión Contractual** es una plataforma modular diseñada para gestionar el ciclo de vida de contratos en la Universidad de los Llanos. Este sistema permite a los usuarios crear, actualizar y administrar contratos de manera eficiente, asegurando un seguimiento adecuado y una gestión documental efectiva.

## Características

- **Gestión de Contratos**: Crear, editar y eliminar contratos.
- **Interfaz Intuitiva**: Diseñada con Tailwind CSS para una experiencia de usuario fluida.
- **Autenticación de Usuarios**: Integración con el sistema de autenticación de Django.
- **Módulos Personalizables**: Estructura modular que permite la expansión de funcionalidades.
- **Soporte para Múltiples Tipos de Contratos**: Gestión de diferentes tipos de contratos y sus respectivas alteraciones.

## Tecnologías Utilizadas

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Base de Datos**: PostgreSQL (recomendado)
- **Contenedores**: Docker
- **Gestión de Archivos**: MinIO (opcional para almacenamiento de archivos)

## Instalación

### Requisitos Previos

- Python 3.11
- Node.js y npm
- Docker y Docker Compose

### Pasos de Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Ripariav/sgc-sistema-gestion-contractual.git
   cd sgc-sistema-gestion-contractual
   Instala las dependencias de Python:

Instala las dependencias de Node.js:
pip install -r requirements.txt

Configura las variables de entorno en un archivo .env (ejemplo en .env.example).

cd theme/static_src
npm install


Ejecuta las migraciones de la base de datos:

Accede a la aplicación en tu navegador en http://localhost:8000.

Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva característica').
Haz push a la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Para más información, puedes contactar a https://www.linkedin.com/in/danielfriverav/