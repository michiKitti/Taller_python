def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

# Solicitar al usuario una frase o palabra
frase = input("Escribe una palabra o frase: ")

# Evaluar si es palíndromo y mostrar el resultado
if es_palindromo(frase):
    print(f"\"{frase}\" es un palíndromo.")
else:
    print(f"\"{frase}\" no es un palíndromo.")
"""
Este programa verifica si una palabra o frase ingresada por el usuario
es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.

No se tienen en cuenta los espacios ni las mayúsculas/minúsculas.
"""
