precio1 = float(input("Precio del primer producto: "))
precio2 = float(input("Precio del segundo producto: "))
precio3 = float(input("Precio del tercer producto: "))

subtotal = precio1 + precio2 + precio3
iva = (subtotal * 15) / 100
total = subtotal + iva

print("Subtotal:", subtotal)
print("IVA (15%):", iva)
print("Total a pagar:", total)
print()
