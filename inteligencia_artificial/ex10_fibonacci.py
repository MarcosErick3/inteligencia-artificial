# Exercício 10: Sequência de Fibonacci
# Imprima os primeiros 10 números da sequência de Fibonacci.

print("Primeiros 10 números da sequência de Fibonacci:")

a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
