# Exercício 41: Remover Duplicatas
# Remova duplicatas de uma lista de números.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros_unicos = list(set(numeros))
numeros_unicos.sort()

print(f"Lista original: {numeros}")
print(f"Lista sem duplicatas: {numeros_unicos}")
