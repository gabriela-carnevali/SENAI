# coding:UTF-8 -*-

print("Olá usuário! Me diga uma temperatura e te direi se o clima está frio, agradável ou quente!")

temp = float(input("Digite a temperatura: "))

if temp < 15:
    print ("O clima está frio.")
elif temp >= 15 and temp <= 25:
    print ("O clima está agradável.")
else:
    print ("O clima está quente.")
