nome = input("Nome do aluno: ")
idade = int(input(f"Idade do(a) {nome}: "))

if idade >= 16:
    print(f"Status: {nome}, você já pode votar! Aproveite sua cidadania.")
else:
    print(f"Status: {nome}, você ainda não tem a idade mínima. Falta pouco!")