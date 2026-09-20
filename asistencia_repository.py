from models.asistencia import Asistencia


class AsistenciaRepository:

    def __init__(self):
        self.asistencias = []

    def crear(self, asistencia: Asistencia):
        self.asistencias.append(asistencia)
        return asistencia

    def obtener_todas(self):
        return self.asistencias

    def obtener_por_id(self, id: int):
        for asistencia in self.asistencias:
            if asistencia.id == id:
                return asistencia
        return None

    def obtener_por_identificacion(self, identificacion: str):
        return [
            asistencia
            for asistencia in self.asistencias
            if asistencia.identificacion == identificacion
        ]

    def actualizar(self, id: int, asistencia_actualizada: Asistencia):
        for posicion, asistencia in enumerate(self.asistencias):
            if asistencia.id == id:
                self.asistencias[posicion] = asistencia_actualizada
                return asistencia_actualizada
        return None

    def eliminar(self, id: int):
        for posicion, asistencia in enumerate(self.asistencias):
            if asistencia.id == id:
                return self.asistencias.pop(posicion)
        return None