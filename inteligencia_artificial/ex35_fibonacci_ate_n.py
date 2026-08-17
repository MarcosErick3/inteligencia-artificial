# Exercício 35: Números Fibonacci Até N
# Gere a sequência de Fibonacci até um número n fornecido pelo usuário.

n = float(input("Digite um número limite: "))

a, b = 0, 1
sequencia = []

while a <= n:
    sequencia.append(a)
    a, b = b, a + b

print(f"Sequência de Fibonacci até {n}:")
print(sequencia)
