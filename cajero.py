"""
Proyecto Final - Reporte de Calificaciones

Este script gestiona un diccionario de estudiantes y sus calificaciones,
calcula promedios, determina estados (Aprobado o Reprobado), y genera un reporte.
"""


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
        calificaciones (list): Lista de números (floats o ints).

    Retorna:
        float: Promedio de las calificaciones.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def obtener_estado(promedio):
    """
    Determina si el promedio es aprobado o reprobado.

    Parámetros:
        promedio (float): Promedio del estudiante.

    Retorna:
        str: "Aprobado" si promedio >= 3.0, "Reprobado" si es menor.
    """
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def generar_reporte(estudiantes):
    """
    Genera un reporte formateado con los nombres, promedios y estados de los estudiantes.

    Parámetros:
        estudiantes (dict): Diccionario con nombres como claves y listas de calificaciones como valores.

    Retorna:
        None
    """
    print("Reporte de Calificaciones:")
    print("-------------------------")
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")
    print("-------------------------")


# Diccionario principal de estudiantes con sus calificaciones
estudiantes = {
    "Ana": [4.5, 4.8, 4.2],
    "Juan": [2.5, 2.8, 3.0],
    "Carlos": [3.0, 3.2, 3.1],
    "María": [5.0, 4.9, 5.0],
    "Lucía": [2.0, 2.3, 1.8]
}

# Llamada a la función principal
generar_reporte(estudiantes)
