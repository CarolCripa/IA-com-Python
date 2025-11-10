'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

'''senha = input("Digite uma senha alfanumerica: ")
tamanho_senha = len(senha) >= 8
numero_senha = any(s.isdigit() for s in senha)
if tamanho_senha and numero_senha:
    print("Senha válida")
else:
    print("Senha Inválida")

    def validar_senha(senha):
    return len(senha) >= 8 and any(s.isdigit() for s in senha)
senha = input("Digite uma senha: ")
while not validar_senha(senha):
    print("Senha inválida, Tente outra.")
    senha = input("Digite uma senha: ")
print("Senha correta.")'''

# Verificador de Senha Segura

# Solicita a senha do usuário
senha = input("Digite uma senha: ")

# Verifica se tem pelo menos 8 caracteres
tem_tamanho = len(senha) >= 8

# Verifica se contém pelo menos um número
tem_numero = any(char.isdigit() for char in senha)

# Verifica se a senha atende aos critérios
if tem_tamanho and tem_numero:
    print("Senha válida! Atende aos critérios de segurança.")
else:
    print("Senha inválida!")
    if not tem_tamanho:
        print("- A senha deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- A senha deve conter pelo menos um número.")


