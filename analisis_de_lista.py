# Lista para guardar los datos del estudiante
estudiantes = []
"""
Este programa solicita el nombre y tres calificaciones de un estudiante,
calcula su promedio y muestra un mensaje según su puntaje.

También guarda la información en una lista de estudiantes y la muestra al final.
"""


# Pedir nombre y validarlo
nombre = input("Ingrese el nombre del estudiante: ")
while nombre.strip() == "":
    nombre = input("El nombre del estudiante no puede estar vacío. Intente de nuevo: ")

# Pedir las calificaciones
calificacion1 = int(input("Ingrese la calificación 1: "))
calificacion2 = int(input("Ingrese la calificación 2: "))
calificacion3 = int(input("Ingrese la calificación 3: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Guardar la información como tupla en la lista
estudiantes.append((nombre, promedio))

# Mostrar resultados
print(f"\nEstudiante: {nombre}")
print(f"Promedio: {promedio:.2f}")

# Clasificación del puntaje
if promedio > 8:
    print("Su puntaje es Alto. ¡Felicitaciones!")
elif promedio < 7:
    print("Su puntaje es Bajo.")
else:
    print("Su puntaje es Medio.")

# Mostrar lista guardada (en este caso, un estudiante)
print("\n Lista de estudiantes:")
for est in estudiantes:
    print(f"{est[0]} - Promedio: {est[1]:.2f}")
