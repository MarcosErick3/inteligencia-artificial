# Exercício 9: Fatorial de um Número
# Calcule o fatorial de um número fornecido pelo usuário.

numero = int(input("Digite um número: "))

if numero < 0:
    print("Fatorial não é definido para números negativos!")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")
