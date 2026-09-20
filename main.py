from fastapi import FastAPI
from routes.asistencia import router as asistencia_router


app = FastAPI(
    title="API Control de Asistencias",
    description="API REST para gestionar la asistencia de estudiantes",
    version="1.0.0"
)


app.include_router(asistencia_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Control de Asistencias funcionando"
    }