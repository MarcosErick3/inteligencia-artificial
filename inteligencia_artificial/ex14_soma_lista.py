# Exercício 14: Soma dos Elementos de uma Lista
# Calcule a soma de todos os elementos em uma lista.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
print(f"Lista: {numeros}")
print(f"Soma dos elementos: {soma}")
