def contar_palabras(texto):
    texto = texto.lower()
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia

# Ejemplo de uso
texto_usuario = input("Escribe un texto: ")
resultado = contar_palabras(texto_usuario)

#  frecuencia de palabras
print("\nFrecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"{palabra}: {cantidad}")
