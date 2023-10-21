# Inicializamos el diccionario de productos
productos = {}

def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad en inventario: "))
    margen_de_ganancia = float(input("Ingrese el margen de ganancia (porcentaje): "))

    precio_venta = costo / (1 - (margen_de_ganancia / 100))
    valor_inventario = costo * cantidad

    producto = {
        "ID": id_producto,
        "Nombre": nombre,
        "Costo": costo,
        "Cantidad": cantidad,
        "Margen de Ganancia": margen_de_ganancia,
        "Precio de Venta": precio_venta,
        "Valor de Inventario": valor_inventario
    }

    productos[id_producto] = producto

def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        for id_producto, producto in productos.items():
            print(f"ID: {id_producto}")
            for clave, valor in producto.items():
                print(f"{clave}: {valor}")
            print("\n")

def ventas():
    if not productos:
        print("No hay productos registrados.")
        return

    id_producto = input("Ingrese el ID del producto a vender: ")

    if id_producto not in productos:
        print("Producto no encontrado.")
        return

    cantidad_vendida = int(input("Ingrese la cantidad a vender: "))

    if cantidad_vendida > productos[id_producto]["Cantidad"]:
        print("No hay suficiente cantidad en inventario para realizar la venta.")
        return

    productos[id_producto]["Cantidad"] -= cantidad_vendida
    print(f"Venta realizada. Se vendieron {cantidad_vendida} unidades de {productos[id_producto]['Nombre']}.")

# Menú de opciones
while True:
    print("\nMenu:")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Ventas")
    print("4. Salir")

    opcion = input("Ingrese su elección (1/2/3/4): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        listar_productos()
    elif opcion == "3":
        ventas()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")