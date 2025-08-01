frase = input("Escribe una frase: ")
vocales = 0
consonantes = 0
for caracter in frase.lower():  # Convierte todo a minúsculas
    if caracter.isalpha():  # Verifica si es una letra (ignora espacios y símbolos)
        if caracter in 'aeiou':
            vocales += 1
        else:
            consonantes += 1

#resultados
print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)
