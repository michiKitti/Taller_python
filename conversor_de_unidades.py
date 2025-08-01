# Diccionario con factores de conversión (a metros)
factores_conversion = {
    "metro": 1,
    "centimetro": 0.01,
    "milimetro": 0.001,
    "kilometro": 1000,
    "pulgada": 0.0254,
    "pie": 0.3048,
    "yarda": 0.9144
}

# Función para convertir entre unidades
def convertir(cantidad, unidad_origen, unidad_destino):
    if unidad_origen not in factores_conversion:
        return f"Unidad de origen '{unidad_origen}' no válida."
    if unidad_destino not in factores_conversion:
        return f"Unidad de destino '{unidad_destino}' no válida."

    # Convertir la cantidad a metros
    en_metros = cantidad * factores_conversion[unidad_origen]

    # Convertir de metros a la unidad de destino
    resultado = en_metros / factores_conversion[unidad_destino]
    return resultado

# Ejemplo de uso
cantidad = float(input("Ingrese la cantidad: "))
origen = input("Unidad de origen: ").lower()
destino = input("Unidad de destino: ").lower()

conversion = convertir(cantidad, origen, destino)

# Mostrar resultado
if isinstance(conversion, str):
    print(conversion)  # Mensaje de error
else:
    print(f"{cantidad} {origen} equivalen a {conversion:.4f} {destino}")
