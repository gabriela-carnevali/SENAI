# -*- coding:UTF-8 -*-

print("Olá usuário! Digite uma temperatura em graus Celsius (°C) e eu transformarei para graus Fahrenheit (ºF) e vice-versa")

temperatura = float(input("Digite a temperatura em graus: "))
medida = str(input("Digite C para Celsius e F para Fahreinheit: "))


def conversao (temperatura, medida):
    conv = 0
    if medida == "C":
        conv = temperatura * 9/5 + 32
        print ("O resultado da conversão é: ", conv)
    elif medida == "F":
        conv = (temperatura - 32) * 5/9
        print ("O resultado da conversão é: ", conv)
conversao(temperatura, medida)
