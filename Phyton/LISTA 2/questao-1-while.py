# -*- coding: UTF-8 -*-

print("Me dê valores e direi a soma e a média dos mesmos. O programa encerra-se quando receber um número negativo")

soma = 0
cont = 0

while True:
    valor = float(input("Digite um valor: "))
    if valor <0:
        print("Você digitou um número negativo, tchau!")
        break
    else:
        soma += valor
        cont += 1
        media = soma / cont
   

print(" A soma é: ", soma)
print("A média é: ", media)
