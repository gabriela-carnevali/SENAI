# -*- coding: UTF-8 -*-

print("Diga a temperatura atual e direi como o clima está hoje")

temp = float(input("Digite a temperatura: "))

if temp < 15:
    print("Está muito frio!")
elif temp >= 16 and temp <23:
    print("Está frio")
elif temp >=23 and temp <26:
    print("Está agradável")
elif temp >= 26 and temp <30:
    print("Está calor")
else:
    print("Está muito quente")
