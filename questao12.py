opcao = 0

while opcao != 5:
    print("1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao >= 1 and opcao <= 4:
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            
            if opcao == 1:
                print(f"Resultado: {n1 + n2}")
            elif opcao == 2:
                print(f"Resultado: {n1 - n2}")
            elif opcao == 3:
                print(f"Resultado: {n1 * n2}")
            elif opcao == 4:
                if n2 != 0:
                    print(f"Resultado: {n1 / n2}")
                else:
                    print("Erro: Não existe divisão por zero!")
                    
        elif opcao == 5:
            print("Saindo...")
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: Digite apenas números!")