# Exercício 45: Par ou Ímpar em Lista
# Classifique os números de uma lista como pares ou ímpares.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(f"\nLista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
