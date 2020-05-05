import random

# Setup inicial
intentos = 3 # Usuario tiene 3 intentos antes de perder
print("Adivina el número entre 1 y 10, 3 oportunidades")
ganaste = False

# El programa genera un número al azar entre 1 y 10
numero_correcto = random.randint(1, 10)

#print("shhhh " + str(numero_correcto)) para probar



# Programa le dice al usuario si su número es mayor o menor al del programa
while intentos > 0:
    numero_usuario = int(input("Adivina el número: "))

    if numero_usuario == numero_correcto:
        print("Correcto, ganaste!")
        ganaste = True
        break
    elif numero_usuario < numero_correcto:
        print("Tu número es MENOR")
    elif numero_usuario > numero_correcto:
        print("Tu número es MAYOR")

    intentos -= 1

if not ganaste:
    print("Perdiste.")
