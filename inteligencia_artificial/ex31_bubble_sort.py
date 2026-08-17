# Exercício 31: Ordenação por Bolha
# Implemente o algoritmo de ordenação por bolha (Bubble Sort).

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"Lista original: {numeros}")
numeros_ordenados = bubble_sort(numeros.copy())
print(f"Lista ordenada: {numeros_ordenados}")
