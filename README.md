# 🔮 Oraculum API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![DeepSeek](https://img.shields.io/badge/AI-DeepSeek--V3-blueviolet?style=for-the-badge)

**Oraculum** es un ecosistema backend de alta fidelidad diseñado para la interpretación mística mediante Inteligencia Artificial. Combina el rigor de la arquitectura de software moderna con el simbolismo del Tarot, la Astrología y la Numerología.

## 🚀 Características Principales

* **Arquitectura Robusta:** Basada en FastAPI con una estructura de servicios desacoplada.
* **Seguridad Bancaria:** Implementación de OAuth2 + JWT para proteger la privacidad de las consultas.
* **IA Avanzada:** Integración nativa con DeepSeek Cloud para interpretaciones profundas y coherentes.
* **Persistencia Inteligente:** Sistema de historial ligado al usuario con almacenamiento en SQLite.
* **Control de Costos:** Sistema integrado de monitoreo de tokens y presupuesto de API.

## 🛠️ Stack Tecnológico

* **Core:** Python 3.13 + FastAPI.
* **ORM:** SQLAlchemy 2.0 (Motores asíncronos preparados).
* **IA:** DeepSeek API (Modelos de Chat y Codificación).
* **Validación:** Pydantic v2 para esquemas de datos estrictos.

## 📂 Estructura del Proyecto (Key Folders)

* `/api`: Endpoints, rutas de autenticación y lógica de la v1.
* `/ai`: Gestión de LLM, control de presupuesto y prompts místicos.
* `/infrastructure`: Capa de base de datos, modelos y configuración de entorno.
* `/services`: El "cerebro" del sistema; coordinadores de motores y repositorios.

## ⚡ Instalación y Uso Rápido

1.  **Clonar y configurar entorno:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt
    ```

2.  **Configurar variables de entorno (.env):**
    ```env
    DEEPSEEK_API_KEY=tu_api_key_aqui
    SECRET_KEY=tu_llave_secreta_para_jwt
    ```

3.  **Lanzar el servidor:**
    ```bash
    uvicorn api.main:app --reload
    ```

## 📖 Documentación de API

Una vez encendido el servidor, accede a:
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **Redoc:** `http://127.0.0.1:8000/redoc`

## 🛡️ Seguridad

El sistema utiliza el flujo de **Bearer Token**. Para cualquier consulta a `/api/v1/`, el encabezado debe incluir:
`Authorization: Bearer <TU_JWT_TOKEN>`

---
*Desarrollado con rigor técnico y visión mística.*
