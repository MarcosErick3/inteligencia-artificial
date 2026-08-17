# Exercício 46: Calcular Média e Desvio Padrão
# Calcule a média e o desvio padrão de uma lista de números.

import math

numeros = []
quantidade = int(input("Quantos números deseja digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    
    # Calcula a variância
    variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desvio_padrao = math.sqrt(variancia)
    
    print(f"\nLista: {numeros}")
    print(f"Média: {media:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
