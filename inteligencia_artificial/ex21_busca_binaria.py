# Exercício 21: Busca Binária
# Implemente a busca binária para encontrar um elemento em uma lista ordenada.

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1

quantidade = int(input("Quantos números deseja digitar? "))
numeros = []

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort()
print(f"\nLista ordenada: {numeros}")

alvo = int(input("Qual número deseja procurar? "))
resultado = busca_binaria(numeros, alvo)

if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}!")
else:
    print("Elemento não encontrado!")
