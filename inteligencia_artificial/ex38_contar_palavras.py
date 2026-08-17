# Exercício 38: Contar Palavras em Texto
# Conte o número de palavras em um texto fornecido pelo usuário.

texto = input("Digite um texto: ")
palavras = texto.split()

print(f"Texto: {texto}")
print(f"Número de palavras: {len(palavras)}")
print(f"Palavras: {palavras}")
