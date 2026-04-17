temperaturas = [28.5, 30.2, 25.0, 22.8, 31.0, 29.5, 27.0]

soma = 0

for t in temperaturas:
    soma = soma + t

media = soma / 7

print(f"Temperaturas: {temperaturas}")
print(f"A média da semana foi de {media:.1f}°C")

if media > 25:
    print("Semana quente!")
else:
    print("Semana agradável.")