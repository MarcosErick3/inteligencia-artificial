# Exercício 37: Funções Recursivas
# Implemente uma função recursiva para calcular o fatorial de um número.

def fatorial_recursivo(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

numero = int(input("Digite um número: "))
resultado = fatorial_recursivo(numero)

if resultado is None:
    print("Fatorial não é definido para números negativos!")
else:
    print(f"O fatorial de {numero} é: {resultado}")
