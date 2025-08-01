"""Sistema de gestión de inventario para una tienda."""

# Lista para almacenar los productos
inventario = []


def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    Solicita nombre, precio y cantidad al usuario.
    """
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.")


def realizar_venta():
    """
    Realiza una venta de un producto.
    Reduce la cantidad disponible del producto en el inventario.
    """
    nombre = input("Ingrese el nombre del producto a vender: ").strip()
    cantidad_vendida = int(input("Cantidad a vender: "))

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total = producto["precio"] * cantidad_vendida
                print(f" Venta realizada. Total a pagar: ${total:.2f}")
            else:
                print("No hay suficiente stock.")
            break
    else:
        print("Producto no encontrado en el inventario.")


def mostrar_inventario():
    """
    Muestra todos los productos en el inventario con su información.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n Inventario actual:")
    for idx, producto in enumerate(inventario, start=1):
        print(f"{idx}. {producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")


# Menú principal
def mostrar_menu():
    """
    Muestra el menú principal de opciones para el usuario.
    """
    while True:
        print("\n==== MENÚ DE INVENTARIO ====")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print(" Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Intente de nuevo.")


# Ejecutar el menú principal
mostrar_menu()
