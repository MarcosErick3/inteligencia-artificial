# Exercício 29: Números FizzBuzz
# Implemente o clássico problema FizzBuzz para números de 1 a 100.

print("FizzBuzz de 1 a 100:")
for numero in range(1, 101):
    if numero % 15 == 0:
        print("FizzBuzz", end=" ")
    elif numero % 3 == 0:
        print("Fizz", end=" ")
    elif numero % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(numero, end=" ")
print()
