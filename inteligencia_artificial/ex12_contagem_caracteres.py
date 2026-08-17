# Exercício 12: Contagem de Caracteres
# Conte o número de ocorrências de cada caractere em uma string fornecida.

texto = input("Digite uma string: ")

print("\nContagem de caracteres:")
for caractere in sorted(set(texto)):
    contagem = texto.count(caractere)
    print(f"'{caractere}': {contagem}")
