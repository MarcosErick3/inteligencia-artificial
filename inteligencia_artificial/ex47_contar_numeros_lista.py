# Exercício 47: Contar Números em Lista
# Conte quantas vezes cada número aparece em uma lista.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

contagem = {}
for numero in numeros:
    contagem[numero] = contagem.get(numero, 0) + 1

print(f"\nLista: {numeros}")
print("Contagem de números:")
for numero, freq in sorted(contagem.items()):
    print(f"{numero}: {freq} vez(es)")
