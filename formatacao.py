estatura = float(input("Digite sua altura: "))
estatura = estatura * 100

#Em Python, f-strigs (f"...) são usadas inserir textos traduzidos dinamicamente dentro de uma frase.

print(f"Sua altura é de {estatura}")
print("Sua altura é de:", estatura )

nome = input("Digite seu nome: ")
idade = 23

texto = "Meu nome é {} e tenho {} anos".format(nome, idade)
texto = "Meu nome é {n} e tenho {i} anos".format(nome, idade)
texto = "Meu nome é %s e tenho %s anos" %(nome, idade)
print(texto) 