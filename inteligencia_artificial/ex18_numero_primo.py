# Exercício 18: Número Primo
# Crie um programa que verifique se um número fornecido é primo.

numero = int(input("Digite um número: "))

if numero < 2:
    print(f"{numero} NÃO é um número primo!")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f"{numero} é um número PRIMO!")
    else:
        print(f"{numero} NÃO é um número primo!")
