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
