TITULO = "===== Atende+ ====="
print(TITULO)

print("Bem-vindo, escolha o que deseja fazer")

# lista para armazenar atendimentos
atendimentos = []

def cadastrarAtendimento():
    print(TITULO)
    
    # validação do nome
    while True:
        nome = input("Informe o nome do cliente: ")
        if nome == "":
            print("Nome não pode ser vazio!")
        else:
            break

    # validação da descrição
    while True:
        descricao = input("Informe o atendimento: ")
        if descricao == "":
            print("Descrição não pode ser vazia!")
        else:
            break

    atendimentos.append({"nome": nome, "descricao": descricao})
    print("Cadastrado com sucesso!\n")


def listarAtendimentos():
    print(TITULO)
    
    if len(atendimentos) == 0:
        print("Nenhum atendimento cadastrado\n")
    else:
        for i, a in enumerate(atendimentos):
            print(i+1, "-", a["nome"], "-", a["descricao"])
        print()


def consultarPorNome():
    print(TITULO)
    
    busca = input("Digite o nome: ")

    if busca == "":
        print("Digite um nome válido\n")
        return

    achou = False

    for a in atendimentos:
        if busca.lower() in a["nome"].lower():
            print(a["nome"], "-", a["descricao"])
            achou = True

    if not achou:
        print("Não encontrado\n")


# menu principal
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Consultar por nome")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrarAtendimento()
    elif op == "2":
        listarAtendimentos()
    elif op == "3":
        consultarPorNome()
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida\n")