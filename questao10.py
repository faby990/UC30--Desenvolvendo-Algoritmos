notas = [5.5, 8.0, 7.5, 4.0, 9.0, 6.5, 10.0]
contador = 0

for n in notas:
    if n > 7:
        contador = contador + 1

print(f"Notas dos alunos: {notas}")
print(f"Quantidade de alunos acima de 7: {contador}")