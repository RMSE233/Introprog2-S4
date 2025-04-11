tareas = float(input("Nota de tareas (30%): "))
parcial = float(input("Nota de examen parcial (30%): "))
final = float(input("Nota de examen final (40%): "))

calificacion_final = (tareas * 0.30) + (parcial * 0.30) + (final * 0.40)

print("Calificación final:", calificacion_final)
print()
