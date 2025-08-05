"""
Este programa recibe un texto del usuario y calcula cuántas veces
aparece cada palabra en ese texto, sin distinguir entre mayúsculas y minúsculas.
"""

def contar_palabras(texto):
    texto = texto.lower()
    palabras = texto.split()
    frecuencia = {}
    """
       Cuenta la frecuencia de cada palabra en un texto.

       Convierte todo el texto a minúsculas, separa las palabras
       y almacena cuántas veces aparece cada una en un diccionario."""
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
