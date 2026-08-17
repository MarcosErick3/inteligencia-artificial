# Exercício 5: Tabuada
# Crie um programa que imprima a tabuada de um número fornecido pelo usuário.

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
