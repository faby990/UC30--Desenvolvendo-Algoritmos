vendas = [120, 155, 200, 343, 450, 600, 711]
soma_pares = 0

for v in vendas:
    if v % 2 == 0:
        soma_pares = soma_pares + v

print(f"Lista de vendas: {vendas}")
print(f"Total das vendas pares: R$ {soma_pares}")