# SGC — Sistema de Gestión Contractual

![Django](https://img.shields.io/badge/Django-Backend-092E20?logo=django&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC?logo=tailwindcss&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Contenedores-2496ED?logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Base%20de%20Datos-4169E1?logo=postgresql&logoColor=white)

Plataforma modular para gestionar el ciclo de vida de contratos en la
**Universidad de los Llanos**. Permite crear, actualizar y administrar
contratos de manera eficiente, con seguimiento y gestión documental.

---

## Características

- Gestión de contratos: crear, editar y eliminar
- Interfaz construida con Tailwind CSS
- Autenticación de usuarios (Django)
- Estructura modular, pensada para expandir funcionalidades
- Soporte para múltiples tipos de contratos y sus alteraciones

---

## Tecnologías

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Base de datos**: PostgreSQL (recomendado)
- **Contenedores**: Docker
- **Archivos**: MinIO (opcional, para almacenamiento)

---

## Instalación

Requisitos previos: Python 3.11, Node.js + npm, Docker y Docker Compose.

```bash
git clone https://github.com/Ripariav/sgc-sistema-gestion-contractual.git
cd sgc-sistema-gestion-contractual

# Dependencias de Python
pip install -r requirements.txt

# Dependencias de Node (Tailwind)
cd theme/static_src && npm install && cd ../..

# Variables de entorno (ver .env.example)
cp .env.example .env

# Migraciones
python manage.py migrate
```

La aplicación queda disponible en `http://localhost:8000`.

---

## Contribuciones

1. Hacé un fork del repositorio
2. Creá una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commiteá tus cambios
4. Hacé push a la rama
5. Abrí un Pull Request

---

## Licencia

MIT — ver [LICENSE](LICENSE).
