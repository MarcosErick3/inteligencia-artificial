# Exercício 32: Jogo da Velha
# Crie um jogo da velha para dois jogadores.

def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(cel == jogador for cel in linha):
            return True
    
    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[lin][col] == jogador for lin in range(3)):
            return True
    
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    return False

def tabuleiro_cheio(tabuleiro):
    return all(cel != " " for linha in tabuleiro for cel in linha)

# Inicializa o jogo
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
jogo_ativo = True

print("=== JOGO DA VELHA ===")
print("Posições: (linha, coluna) começando de 0")

while jogo_ativo:
    exibir_tabuleiro(tabuleiro)
    
    # Pede jogada do jogador atual
    while True:
        try:
            linha = int(input(f"Jogador {jogador_atual}, digite a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador_atual}, digite a coluna (0-2): "))
            
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida!")
                continue
            
            if tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada!")
                continue
            
            tabuleiro[linha][coluna] = jogador_atual
            break
        except ValueError:
            print("Entrada inválida! Digite números entre 0 e 2.")
    
    # Verifica se ganhou
    if verificar_vencedor(tabuleiro, jogador_atual):
        exibir_tabuleiro(tabuleiro)
        print(f"🎉 Jogador {jogador_atual} venceu!")
        jogo_ativo = False
    elif tabuleiro_cheio(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        print("Empate!")
        jogo_ativo = False
    else:
        # Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
