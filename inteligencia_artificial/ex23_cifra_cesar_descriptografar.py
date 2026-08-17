# Exercício 23: Descriptografar Cifra de César
# Crie uma função para descriptografar uma mensagem cifrada com a cifra de César.

def cifra_cesar_descriptografar(mensagem, deslocamento):
    resultado = ""
    
    for caractere in mensagem:
        if caractere.isalpha():
            if caractere.isupper():
                resultado += chr((ord(caractere) - ord('A') - deslocamento) % 26 + ord('A'))
            else:
                resultado += chr((ord(caractere) - ord('a') - deslocamento) % 26 + ord('a'))
        else:
            resultado += caractere
    
    return resultado

mensagem_criptografada = input("Digite a mensagem a descriptografar: ")
deslocamento = int(input("Digite o deslocamento usado na criptografia (1-25): "))

mensagem_descriptografada = cifra_cesar_descriptografar(mensagem_criptografada, deslocamento)
print(f"Mensagem criptografada: {mensagem_criptografada}")
print(f"Mensagem descriptografada: {mensagem_descriptografada}")
