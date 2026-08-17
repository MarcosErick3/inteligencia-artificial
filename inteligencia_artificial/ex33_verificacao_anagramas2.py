# Exercício 33: Verificação de Anagramas
# Verifique se duas palavras fornecidas são anagramas uma da outra.

def sao_anagramas(palavra1, palavra2):
    palavra1 = ''.join(filter(str.isalpha, palavra1.lower()))
    palavra2 = ''.join(filter(str.isalpha, palavra2.lower()))
    
    return sorted(palavra1) == sorted(palavra2)

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_anagramas(palavra1, palavra2):
    print(f"'{palavra1}' e '{palavra2}' SÃO anagramas!")
else:
    print(f"'{palavra1}' e '{palavra2}' NÃO são anagramas!")
