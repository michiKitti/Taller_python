# Saldo inicial del usuario
saldo = 1000.0
"""
Este programa simula un cajero automático simple.
Permite consultar el saldo, depositar dinero y retirar dinero,
manejando un saldo inicial fijo para el usuario.
"""


def consultar_saldo():
    """Muestra el saldo actual."""
    print(f"Saldo actual: ${saldo:.2f}")


def depositar():
    """Permite al usuario depositar dinero en su cuenta."""
    global saldo
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    else:
        print("El monto debe ser mayor que cero.")


def retirar():
    """Permite al usuario retirar dinero si hay saldo suficiente."""
    global saldo
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
    elif monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")


def mostrar_menu():
    """Muestra el menú de opciones del cajero automático."""
    while True:
        print("\n=== MENÚ CAJERO ===")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Sesión finalizada.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
mostrar_menu()
