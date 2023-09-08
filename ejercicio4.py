numero_telefono = input("Ingresa un número de teléfono con formato +34-XXXXXXXX-XX: ")

numero_sin_prefijo_extension = numero_telefono[4:14]

print("El número de teléfono sin el prefijo y la extensión es:", numero_sin_prefijo_extension)
