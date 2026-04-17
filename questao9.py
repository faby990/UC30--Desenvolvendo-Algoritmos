notas = [5.5, 8.0, 7.5, 4.0, 9.0, 6.5, 10.0]

aprovados = 0

for n in notas:
    if n > 7:
        aprovados = aprovados + 1

print(f"Notas: {notas}")
print(f"Total de alunos com nota acima de 7: {aprovados}")