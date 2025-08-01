# Diccionario para guardar los contactos
agenda = {}


# Función para añadir un nuevo contacto
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' añadido correctamente.")


# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f" El número de {nombre} es: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")


# Función para mostrar todos los contactos
def mostrar_contactos():
    if len(agenda) == 0:
        print(" La agenda está vacía.")
    else:
        print(" Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")


# Menú principal
while True:
    print("\n AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == "2":
        nombre = input("Nombre del contacto a buscar: ")
        buscar_contacto(nombre)

    elif opcion == "3":
        mostrar_contactos()

    elif opcion == "4":
        print(" Cerrando la agenda. ¡Hasta luego!")
        break

    else:
        print(" Opción no válida. Intenta de nuevo.")
