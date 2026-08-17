# Exercício 43: Conversor de Unidades
# Converta unidades de comprimento (por exemplo, metros para centímetros).

print("=== CONVERSOR DE UNIDADES DE COMPRIMENTO ===")
print("Conversões disponíveis:")
print("1. Metros para Centímetros")
print("2. Centímetros para Metros")
print("3. Metros para Quilômetros")
print("4. Quilômetros para Metros")
print("5. Metros para Milímetros")
print("6. Milímetros para Metros")

opcao = input("\nEscolha uma conversão: ")
valor = float(input("Digite o valor a converter: "))

if opcao == "1":
    resultado = valor * 100
    print(f"{valor} m = {resultado} cm")
elif opcao == "2":
    resultado = valor / 100
    print(f"{valor} cm = {resultado} m")
elif opcao == "3":
    resultado = valor / 1000
    print(f"{valor} m = {resultado} km")
elif opcao == "4":
    resultado = valor * 1000
    print(f"{valor} km = {resultado} m")
elif opcao == "5":
    resultado = valor * 1000
    print(f"{valor} m = {resultado} mm")
elif opcao == "6":
    resultado = valor / 1000
    print(f"{valor} mm = {resultado} m")
else:
    print("Opção inválida!")
