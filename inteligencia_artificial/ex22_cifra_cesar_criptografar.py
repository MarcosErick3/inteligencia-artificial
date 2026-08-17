# Exercício 22: Criptografia de Cifra de César
# Crie uma função para criptografar uma mensagem usando a cifra de César.

def cifra_cesar_criptografar(mensagem, deslocamento):
    resultado = ""
    
    for caractere in mensagem:
        if caractere.isalpha():
            if caractere.isupper():
                resultado += chr((ord(caractere) - ord('A') + deslocamento) % 26 + ord('A'))
            else:
                resultado += chr((ord(caractere) - ord('a') + deslocamento) % 26 + ord('a'))
        else:
            resultado += caractere
    
    return resultado

mensagem = input("Digite a mensagem a criptografar: ")
deslocamento = int(input("Digite o deslocamento (1-25): "))

mensagem_criptografada = cifra_cesar_criptografar(mensagem, deslocamento)
print(f"Mensagem original: {mensagem}")
print(f"Mensagem criptografada: {mensagem_criptografada}")
