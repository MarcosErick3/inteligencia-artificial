# Exercício 39: Jogo de Dados
# Simule o lançamento de dois dados e mostre o resultado.

import random

print("=== LANÇAMENTO DE DADOS ===")
print("Você vai lançar dois dados!")

input("Pressione ENTER para lançar... ")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2

print(f"\nDado 1: {dado1}")
print(f"Dado 2: {dado2}")
print(f"Soma: {soma}")

if soma == 7 or soma == 11:
    print("🎉 Você ganhou!")
elif soma == 2 or soma == 3 or soma == 12:
    print("😢 Você perdeu!")
else:
    print("O jogo continua...")
