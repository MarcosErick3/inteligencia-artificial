# Exercício 17: Dicionário de Contagem de Palavras
# Conte a frequência de cada palavra em uma string fornecida pelo usuário.

texto = input("Digite um texto: ").lower()
palavras = texto.split()

contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print("\nFrequência de palavras:")
for palavra, freq in sorted(contagem.items()):
    print(f"'{palavra}': {freq}")
