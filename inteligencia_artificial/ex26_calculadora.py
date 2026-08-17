# Exercício 26: Calculadora Simples
# Crie uma calculadora que possa realizar adição, subtração, multiplicação e divisão.

print("=== CALCULADORA SIMPLES ===")
print("Operações disponíveis:")
print("+ Adição")
print("- Subtração")
print("* Multiplicação")
print("/ Divisão")

num1 = float(input("\nDigite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Erro: Divisão por zero!")
    else:
        resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print(f"\n{num1} {operacao} {num2} = {resultado}")
