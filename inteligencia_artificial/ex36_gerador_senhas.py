# Exercício 36: Gerador de Senhas
# Crie um gerador de senhas aleatórias com letras e números.

import random
import string

comprimento = int(input("Digite o comprimento da senha (mínimo 8): "))

if comprimento < 8:
    print("A senha deve ter no mínimo 8 caracteres!")
else:
    # Caracteres disponíveis
    letras = string.ascii_letters
    numeros = string.digits
    
    # Gera senha
    senha = []
    
    # Adiciona pelo menos 1 letra
    senha.append(random.choice(letras))
    # Adiciona pelo menos 1 número
    senha.append(random.choice(numeros))
    
    # Completa com caracteres aleatórios
    caracteres = letras + numeros
    for _ in range(comprimento - 2):
        senha.append(random.choice(caracteres))
    
    # Embaralha
    random.shuffle(senha)
    senha_final = ''.join(senha)
    
    print(f"Senha gerada: {senha_final}")
