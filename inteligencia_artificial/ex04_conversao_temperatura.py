# Exercício 4: Conversão de Temperatura
# Converta uma temperatura fornecida em Celsius para Fahrenheit usando a fórmula F = C * 9/5 + 32.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
