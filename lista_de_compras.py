# Inicializamos la lista vacía
lista_compras = []

# Menú principal usando un bucle while
while True:
    print("\n MENÚ - Lista de Compras")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        item = input("Escribe el nombre del ítem que deseas agregar: ")
        lista_compras.append(item)
        print(f" '{item}' ha sido agregado a la lista.")

    elif opcion == "2":
        item = input("Escribe el nombre del ítem que deseas eliminar: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f" '{item}' ha sido eliminado de la lista.")
        else:
            print(f"'{item}' no está en la lista.")

    elif opcion == "3":
        if len(lista_compras) == 0:
            print(" La lista de compras está vacía.")
        else:
            print("\n Tu lista de compras:")
            for i, producto in enumerate(lista_compras, start=1):
                print(f"{i}. {producto}")

    elif opcion == "4":
        print(" ¡Gracias por usar la lista de compras! Hasta pronto.")
        break

    else:
        print(" Opción no válida. Por favor, elige entre 1 y 4.")
