# Exercício 30: Jogo da Forca
# Desenvolva um jogo simples da forca onde o usuário deve adivinhar uma palavra.

import random

palavras = ["python", "programacao", "computador", "inteligencia", "artificial", "desenvolvimento"]
palavra_sorteada = random.choice(palavras).upper()
letras_adivinhadas = []
tentativas = 6

print("=== JOGO DA FORCA ===")
print(f"A palavra tem {len(palavra_sorteada)} letras")

while tentativas > 0:
    # Mostra a palavra com as letras adivinhadas
    palavra_exibida = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_sorteada])
    print(f"\nPalavra: {' '.join(palavra_exibida)}")
    print(f"Letras adivinhadas: {', '.join(sorted(letras_adivinhadas))}")
    print(f"Tentativas restantes: {tentativas}")
    
    # Verifica se ganhou
    if palavra_exibida == palavra_sorteada:
        print(f"\n🎉 Parabéns! Você adivinhou a palavra: {palavra_sorteada}")
        break
    
    # Pede uma letra
    letra = input("Digite uma letra: ").upper()
    
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra!")
    elif letra in palavra_sorteada:
        letras_adivinhadas.append(letra)
        print("Acertou!")
    else:
        letras_adivinhadas.append(letra)
        tentativas -= 1
        print("Errou!")
else:
    print(f"\n😢 Game Over! A palavra era: {palavra_sorteada}")
