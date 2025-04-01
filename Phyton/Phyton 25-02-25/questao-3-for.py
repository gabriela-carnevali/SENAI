# -*- coding: UTF-8 -*-

print ("Digite números positivos e eu farei a média deles")

soma = 0
quant = int(input("Digite a quantidade de vezes que quer repetir: "))

for i in range (quant):
    valor = float(input("Digite um valor: "))
    soma += valor

media = soma / quant

print("A média é igual a: %.2f" %media)
