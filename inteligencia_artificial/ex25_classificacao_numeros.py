# Exercício 25: Classificação de Números
# Classifique uma lista de números em três categorias: positivos, negativos e zeros.

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

positivos = [n for n in numeros if n > 0]
negativos = [n for n in numeros if n < 0]
zeros = [n for n in numeros if n == 0]

print(f"\nNúmeros positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Zeros: {zeros}")
print(f"\nTotal de positivos: {len(positivos)}")
print(f"Total de negativos: {len(negativos)}")
print(f"Total de zeros: {len(zeros)}")
