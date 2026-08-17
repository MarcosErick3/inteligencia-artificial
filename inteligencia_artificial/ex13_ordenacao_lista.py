# Exercício 13: Ordenação de Lista
# Dada uma lista de números, ordene-a em ordem crescente.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort()
print(f"Lista ordenada em ordem crescente: {numeros}")
