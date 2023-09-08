precio = float(input("Ingresa el precio del producto en euros con dos decimales: "))

euros = int(precio)
centimos = int((precio - euros) * 100)

print("El precio ingresado es de", euros, "euros y", centimos,)
