def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
   
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta"
    else:
        return "Usuário inválido"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
tentativas = int(input("Digite o número de tentativas: "))

print(verificar_acesso(usuario, senha, tentativas))