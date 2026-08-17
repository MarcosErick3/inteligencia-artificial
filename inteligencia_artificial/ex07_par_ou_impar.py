# Exercício 7: Número Ímpar ou Par
# Solicite um número ao usuário e informe se ele é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número PAR")
else:
    print(f"{numero} é um número ÍMPAR")
