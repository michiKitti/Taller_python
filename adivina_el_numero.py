
# Número secreto definido estáticamente
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
