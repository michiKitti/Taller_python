"""
Este programa es un juego donde el usuario debe adivinar un número secreto entre 1 y 100.
El número secreto está definido dentro del código. El usuario recibe pistas hasta acertar.
"""
# Número secreto definido estáticamente
def jugar_adivinanza():
    """
    Inicia un juego de adivinanza donde el usuario intenta adivinar un número secreto.
    El programa valida si el número está en el rango correcto (1 a 100) y da pistas
    sobre si el número ingresado es mayor o menor que el número secreto.

    No recibe parámetros y no retorna ningún valor.
    """
numero_secreto = 42
# Inicializamos la variable del intento del usuario
intento = 0
while intento != numero_secreto:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento < 1 or intento > 100:
        print("El número está fuera de rango. Intenta de nuevo.")
    elif intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print(" Demasiado alto.")
# Mensaje final cuando el número es correcto
print("¡Felicidades! Adivinaste el número secreto.")
