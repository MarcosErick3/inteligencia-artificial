# Exercício 27: Anagramas
# Verifique se duas palavras são anagramas (ou seja, se são formadas pelas mesmas letras).

palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

# Remove espaços
palavra1 = palavra1.replace(" ", "")
palavra2 = palavra2.replace(" ", "")

if sorted(palavra1) == sorted(palavra2):
    print(f"'{palavra1}' e '{palavra2}' SÃO anagramas!")
else:
    print(f"'{palavra1}' e '{palavra2}' NÃO são anagramas!")
