def analisar(palavra, numero):
    quantidade = len(palavra)

    if numero > 0:
     tipo = "positivo"
    elif numero < 0:
       tipo = "negativo"
    else:
       tipo = "zero"

    return quantidade, tipo
letras, resultado = analisar("amor", 5)
print(letras)
print(resultado)