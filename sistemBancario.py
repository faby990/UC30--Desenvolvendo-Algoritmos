def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
   
    if saque > 1000:
        taxa = saque * 0.02
        saque_total = saque + taxa
    else:
        saque_total = saque

    saldo_restante = saldo - saque_total
    return saldo_restante

saldo = float(input("Digite seu saldo: "))
saque = float(input("Digite o valor do saque: "))

print(saldo_final(saldo, saque))