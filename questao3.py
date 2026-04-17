total = 0.0
valor = float(input("Digite o valor do item (ou 0 para sair): "))

while valor != 0:
    total = total + valor
    valor = float(input("Digite o valor do próximo item (ou 0 para sair): "))

print(f"Total da compra: R$ {total:.2f}")