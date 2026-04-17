def calcular_imc():
    try:
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (ex: 1.75): "))
        
        imc = peso / (altura * altura)
        
        print(f"Seu IMC é: {imc:.1f}")
        
        if imc < 18.5:
            print("Categoria: Magro")
        elif imc <= 24.9:
            print("Categoria: Normal")
        else:
            print("Categoria: Sobrepeso")
            
    except ValueError:
        print("Erro: Digite apenas números usando ponto.")

calcular_imc()