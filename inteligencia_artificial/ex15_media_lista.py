# Exercício 15: Média de uma Lista
# Calcule a média dos números em uma lista.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"Lista: {numeros}")
    print(f"Média dos números: {media:.2f}")
