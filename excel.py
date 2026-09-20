from openpyxl import load_workbook

from models.asistencia import Asistencia


RUTA_EXCEL = r"E:\ControlAsistencias\Control_Asistencias.xlsx"


def guardar_asistencia(asistencia: Asistencia):

    # Abrir el archivo Excel
    libro = load_workbook(RUTA_EXCEL)

    # Seleccionar la hoja activa
    hoja = libro.active

    # Agregar la asistencia como una nueva fila
    hoja.append([
        asistencia.id,
        asistencia.identificacion,
        asistencia.nombre,
        asistencia.asignatura,
        str(asistencia.fecha),
        str(asistencia.hora),
        asistencia.estado.value
    ])

    # Guardar los cambios
    libro.save(RUTA_EXCEL)

    return True