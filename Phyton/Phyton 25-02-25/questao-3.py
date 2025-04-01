# -*- coding: UTF-8 -*-

print("Digite valores positivos e eu farei a média. Caso um valor negativo seja digitado, a conta finaliza")

valor = 0
cont = 0
while True:
    valor = float(input("Digite um valor positivo: "))
    if valor < 0:
        print("Você escolheu sair, tchau!")
        break
    cont = cont + 1
    resultado = valor * cont / cont
print("A média é: ", resultado)
