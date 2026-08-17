# Exercício 28: Gráfico de Barras
# Use a biblioteca matplotlib para criar um gráfico de barras com dados fornecidos pelo usuário.

import matplotlib.pyplot as plt

quantidade_dados = int(input("Quantos dados deseja adicionar? "))

labels = []
valores = []

for i in range(quantidade_dados):
    label = input(f"Digite o rótulo do {i+1}º dado: ")
    valor = float(input(f"Digite o valor de '{label}': "))
    labels.append(label)
    valores.append(valor)

plt.figure(figsize=(10, 5))
plt.bar(labels, valores, color='blue', alpha=0.7)
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.show()
