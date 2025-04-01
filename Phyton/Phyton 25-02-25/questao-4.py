# -*- coding: UTF-8 -*-

print("Digite números e direi quantos deles estão entre 100 e 200. Quando o valor 0 for digitado, a contagem se findará.")

cont = 0

while True:
    num = float(input("Digite um número: "))
    if num == 0:
        print("Você escolheu sair, tchau!")
        break
    elif num >=100 and num <201:
        cont += 1
        
print ("A quantidade de números entre 100 e 200 é: ", cont)
