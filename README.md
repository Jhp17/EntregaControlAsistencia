# API Control de Asistencias

## Descripción

Este proyecto consiste en una API REST desarrollada con Python y FastAPI para registrar y consultar la asistencia de estudiantes a clases.

La aplicación permite realizar diferentes operaciones sobre los registros de asistencia y también cuenta con integración con Excel y Telegram.

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- OpenPyXL
- Telegram Bot
- GitHub

## Información de una asistencia

Cada registro contiene:

- ID
- Identificación del estudiante
- Nombre
- Asignatura
- Fecha
- Hora
- Estado

Los estados permitidos son:

- PRESENTE
- AUSENTE
- TARDE

## Funcionalidades

La API permite:

- Registrar una asistencia.
- Consultar todas las asistencias.
- Consultar una asistencia por ID.
- Actualizar una asistencia.
- Eliminar una asistencia.
- Consultar el porcentaje de asistencia de un estudiante.
- Guardar los registros en Excel.
- Registrar asistencias mediante Telegram.

## Endpoints principales

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Verifica que la API esté funcionando. |
| POST | `/asistencia/` | Registra una nueva asistencia. |
| GET | `/asistencia/` | Consulta todas las asistencias. |
| GET | `/asistencia/{id}` | Consulta una asistencia por ID. |
| PUT | `/asistencia/{id}` | Actualiza una asistencia. |
| DELETE | `/asistencia/{id}` | Elimina una asistencia. |
| GET | `/asistencia/{identificacion}/porcentaje` | Calcula el porcentaje de asistencia. |

## Estructura del proyecto

```text
EntregaControlAsistencia/
│
├── main.py
├── telegram_bot.py
├── asistencia.py
├── asistencia_service.py
├── asistencia_repository.py
├── excel.py
├── requirements.txt
├── README.md
└── tests/
```

## Instalación

Primero se debe tener Python instalado.

Luego se instalan las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar la API se utiliza:

```bash
uvicorn main:app --reload
```

La documentación automática de FastAPI estará disponible en:

```text
http://127.0.0.1:8000/docs
```

## Registro de asistencia

Un registro de asistencia contiene información como la identificación del estudiante, nombre, asignatura, fecha, hora y estado.

Ejemplo:

```json
{
  "identificacion": "1000001",
  "nombre": "Juan Perez",
  "asignatura": "Estructuras de Datos",
  "fecha": "2026-09-20",
  "hora": "15:00",
  "estado": "PRESENTE"
}
```

## Porcentaje de asistencia

El sistema permite consultar el porcentaje de asistencia de un estudiante utilizando sus registros almacenados.

Endpoint:

```text
GET /asistencia/{identificacion}/porcentaje
```

El cálculo se realiza a partir de las asistencias registradas.

## Integración con Excel

El proyecto utiliza Excel para conservar el historial de las asistencias registradas.

El archivo utilizado para almacenar la información es:

```text
Control_Asistencias.xlsx
```

## Integración con Telegram

El archivo `telegram_bot.py` contiene la lógica relacionada con el bot de Telegram.

El bot permite solicitar los datos de una asistencia y enviarlos a la API para realizar el registro.

Las credenciales utilizadas por Telegram deben mantenerse privadas y no deben publicarse dentro del repositorio.

## Pruebas

El proyecto debe comprobar el funcionamiento de las principales operaciones de la API, incluyendo:

- Registro.
- Consulta.
- Actualización.
- Eliminación.
- Cálculo del porcentaje.
- Validación de datos.
- Integración con Excel.
- Integración con Telegram.
- Manejo de errores.

## Objetivo

El objetivo del proyecto es aplicar los conceptos de API REST, separación de responsabilidades, persistencia de información e integración con servicios externos mediante una aplicación desarrollada con FastAPI.

## Integrantes

Jhon Oyola 
Yesenia Perez
Ramiro Montiel
Jose perez
