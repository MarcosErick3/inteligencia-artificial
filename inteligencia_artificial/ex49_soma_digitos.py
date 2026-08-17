# Exercício 49: Soma dos Dígitos
# Calcule a soma dos dígitos de um número inteiro fornecido.

numero = int(input("Digite um número inteiro: "))

# Trabalha com o valor absoluto para números negativos
numero_abs = abs(numero)
soma_digitos = sum(int(digito) for digito in str(numero_abs))

print(f"Número: {numero}")
print(f"Soma dos dígitos: {soma_digitos}")
