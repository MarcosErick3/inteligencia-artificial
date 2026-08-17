# Exercício 3: Cálculo da Área do Círculo
# Solicite o raio de um círculo e calcule sua área. Use a fórmula área = π * r².

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)

print(f"A área do círculo com raio {raio} é: {area:.2f}")
