# -*- coding: UTF-8 -*-

num = 0
print ("""Digite números positivos e direi a quantidade de números que digitou.
Caso digite um número negativo, a contagem finaliza: """)

while True:
    valor = int(input("Digite um valor: "))
    if valor <0:
        print("Você escolheu sair, tchau!")
        break
    num = num + 1
print("A quantidade de valores é: ", num)
