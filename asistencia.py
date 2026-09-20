from pydantic import BaseModel
from enum import Enum
from datetime import date, time


class EstadoAsistencia(str, Enum):
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"
    TARDE = "TARDE"


class Asistencia(BaseModel):
    id: int
    identificacion: str
    nombre: str
    asignatura: str
    fecha: date
    hora: time
    estado: EstadoAsistencia