import random

numeros = [10, 20, 30, 20, 40, 20, 50]
print("Lista númerica: ", numeros)

print("Quantidade de números presente na lista: ", len(numeros)) 

print("Quantas vezes o número 20 aparece na lista?: ", numeros.count(20)) 

print("Em que posição aparece o número 30 na lista? ", numeros.index(30)) 

print("Existe número 100 na lista?", 100 in numeros) 

numeros2 = [91, 34, 67, 15, 82]
print("Lista númerica original: ", numeros)

numeros2.sort()
print("Lista ordem crescente: ", numeros2)

numeros2.sort(reverse=True)
print("Lista ordem decrescente: ", numeros2) 

numeros3 = [80, 7, 10, 9, 19] 
print("Lista atualizada: ", numeros3)

random.shuffle(numeros3)
print("Embaralhar: ", numeros3) 

numeros4 = [10, 21, 45, 23, 76, 98]
print("Minha lista: ", numeros4)

numeros4.sort()
print("Lista ordem crescente: ", numeros4)

numeros4.sort(reverse=True)
print("Lista ordem decrescente: ", numeros4) 

random.shuffle(numeros4)
print("Embaralhar: ", numeros4) 