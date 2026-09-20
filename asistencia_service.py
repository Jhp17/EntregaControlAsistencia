from models.asistencia import Asistencia
from repositories.asistencia_repository import AsistenciaRepository
from integrations.excel import guardar_asistencia


class AsistenciaService:

    def __init__(self, repository: AsistenciaRepository):
        self.repository = repository

    def registrar_asistencia(self, asistencia: Asistencia):
        # Guardar en el repositorio
        resultado = self.repository.crear(asistencia)

        # Guardar también en Excel
        guardar_asistencia(asistencia)

        return resultado

    def obtener_asistencias(self):
        return self.repository.obtener_todas()

    def obtener_asistencia(self, id: int):
        return self.repository.obtener_por_id(id)

    def actualizar_asistencia(self, id: int, asistencia: Asistencia):
        return self.repository.actualizar(id, asistencia)

    def eliminar_asistencia(self, id: int):
        return self.repository.eliminar(id)

    def calcular_porcentaje(self, identificacion: str):
        asistencias = self.repository.obtener_por_identificacion(
            identificacion
        )

        if not asistencias:
            return 0

        total = len(asistencias)

        presentes = sum(
            1
            for asistencia in asistencias
            if asistencia.estado.value in ["PRESENTE", "TARDE"]
        )

        porcentaje = (presentes / total) * 100

        return round(porcentaje, 2)