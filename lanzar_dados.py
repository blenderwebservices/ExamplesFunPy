import random

def lanzar_dados():
    print("\nSimulando el lanzamiento de dos dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Resultados: Dado 1 = {dado1}, Dado 2 = {dado2}")
    print(f"Suma total: {dado1 + dado2}\n")
    new_var = input("pulsa Enter para continuar ... \n")