#Adivinar un numero
import random

numero = random.randint(1,10)
while(True):
    numero_usuario = int(input("Dime un numero del 1 al 10: "))
    if(numero_secreto == numero_usuario):
        print(f"Felicidades, adivinaste el numero secreto: {numero_usuario}")
        break
    else: 
        print("sigue intentando")
        if(numero_usuario > numero_secreto):
            print("el numero es menor pedazo de animal")
        else:
            print("el numero es mayor")