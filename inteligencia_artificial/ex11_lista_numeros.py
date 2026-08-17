# Exercício 11: Lista de Números
# Crie uma lista de números e exiba o maior e o menor número.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

if numeros:
    print(f"Lista: {numeros}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
