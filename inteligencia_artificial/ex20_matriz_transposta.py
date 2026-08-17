# Exercício 20: Matriz Transposta
# Dada uma matriz (lista de listas), crie sua matriz transposta.

linhas = int(input("Quantas linhas tem a matriz? "))
colunas = int(input("Quantas colunas tem a matriz? "))

matriz = []
print("Digite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elem = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(elem)
    matriz.append(linha)

# Transposta
transposta = [[matriz[i][j] for i in range(linhas)] for j in range(colunas)]

print("\nMatriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)
