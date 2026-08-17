# Exercício 44: Fibonacci em Nível
# Gere a sequência de Fibonacci até um determinado número de termos.

numero_termos = int(input("Quantos termos da sequência de Fibonacci deseja? "))

if numero_termos <= 0:
    print("O número de termos deve ser maior que 0!")
else:
    sequencia = []
    a, b = 0, 1
    
    for _ in range(numero_termos):
        sequencia.append(a)
        a, b = b, a + b
    
    print(f"Primeiros {numero_termos} números de Fibonacci:")
    print(sequencia)
