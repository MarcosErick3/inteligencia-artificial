# Exercício 34: Contador de Vogais
# Conte o número de vogais em uma string fornecida.

texto = input("Digite um texto: ").lower()
vogais = "aeiouáéíóúã"

contagem = 0
detalhes = {}

for vogal in vogais:
    if vogal in texto:
        count = texto.count(vogal)
        detalhes[vogal] = count
        contagem += count

print(f"\nTexto: {texto}")
print(f"Total de vogais: {contagem}")
print("\nDetalhes:")
for vogal, count in sorted(detalhes.items()):
    print(f"'{vogal}': {count}")
