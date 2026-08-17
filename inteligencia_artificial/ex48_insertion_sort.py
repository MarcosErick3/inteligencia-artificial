# Exercício 48: Ordenação por Inserção
# Implemente o algoritmo de ordenação por inserção (Insertion Sort).

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"Lista original: {numeros}")
numeros_ordenados = insertion_sort(numeros.copy())
print(f"Lista ordenada: {numeros_ordenados}")
