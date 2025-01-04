import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\n¡Adivina el número entre 1 y 100!")
    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        if intento < numero_secreto:
            print("¡Muy bajo!")
        elif intento > numero_secreto:
            print("¡Muy alto!")
        else:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.\n")
            new_var = input("pulsa Enter para continuar ... \n")
            
            break