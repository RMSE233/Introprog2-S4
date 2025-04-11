nombre_producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento: "))

descuento_aplicado = (precio * descuento) / 100
precio_final = precio - descuento_aplicado

print("Producto:", nombre_producto)
print("Precio final con descuento:", precio_final)
print()
