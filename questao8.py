valor = float(input("Valor da compra: R$ "))

if valor > 500:
    desconto = valor * 0.20
elif valor >= 200:
    desconto = valor * 0.10
else:
    desconto = 0

total = valor - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")