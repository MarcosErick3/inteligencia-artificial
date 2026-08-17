# Exercício 42: Números Primos até N
# Gere todos os números primos até um número n fornecido.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Digite um número: "))
primos = [num for num in range(2, n + 1) if eh_primo(num)]

print(f"Números primos até {n}:")
print(primos)
print(f"Total de primos: {len(primos)}")
