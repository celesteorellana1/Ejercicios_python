productos = input("Ingresa los productos de tu cesta de compra, separados por comas: ")

lista_productos = productos.split(",")

for producto in lista_productos:
    print(producto.strip())