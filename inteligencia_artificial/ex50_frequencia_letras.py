# Exercício 50: Cálculo de Frequência de Letras
# Calcule a frequência de cada letra em uma string fornecida pelo usuário.

texto = input("Digite um texto: ").lower()

# Remove espaços e caracteres especiais, mantém apenas letras
letras = [c for c in texto if c.isalpha()]

frequencia = {}
for letra in letras:
    frequencia[letra] = frequencia.get(letra, 0) + 1

print(f"\nTexto: {texto}")
print("Frequência de letras:")
for letra in sorted(frequencia.keys()):
    print(f"'{letra}': {frequencia[letra]}")
