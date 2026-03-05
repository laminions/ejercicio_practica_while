import random

numero = random.randint(1, 100)
intento = 0

while intento != numero:
    intento = int(input("adivina el numero desde el 1 hasta el 100: "))

    if intento < numero:
        print("el numero es mas alto")
    elif intento > numero:
        print("el numero es mas abajo")

print("felicidades has adivinado elnumero :)")
