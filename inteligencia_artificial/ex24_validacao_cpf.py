# Exercício 24: Validação de CPF
# Implemente uma função para validar um CPF brasileiro.

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    digito1 = 0 if digito1 > 9 else digito1
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    digito2 = 0 if digito2 > 9 else digito2
    
    # Verifica se os dígitos verificadores estão corretos
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

cpf = input("Digite um CPF (com ou sem formatação): ")

if validar_cpf(cpf):
    print("CPF VÁLIDO!")
else:
    print("CPF INVÁLIDO!")
