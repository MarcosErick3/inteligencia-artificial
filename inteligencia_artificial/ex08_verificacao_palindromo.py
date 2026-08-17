# Exercício 8: Verificação de Palíndromo
# Crie um programa que verifique se uma palavra é um palíndromo (ex: "radar").

palavra = input("Digite uma palavra: ").lower()

if palavra == palavra[::-1]:
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' NÃO é um palíndromo!")
