# Exercício 19: Jogo de Adivinhação
# Implemente um jogo onde o usuário deve adivinhar um número gerado aleatoriamente pelo computador.

import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Bem-vindo ao Jogo de Adivinhação!")
print("Pense em um número entre 1 e 100 e tente adivinhar!")

while not acertou:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if tentativa < numero_secreto:
        print("O número é MAIOR! Tente novamente.")
    elif tentativa > numero_secreto:
        print("O número é MENOR! Tente novamente.")
    else:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
