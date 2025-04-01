# -*- coding: UTF-8 -*-

print("Digite idade e direi quantas tem menos de 21 anos e quantas tem mais de 50")

m21= 0
M50 = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade == -99:
        print("Você decidiu sair, tchau!")
        break
    elif idade < 21:
        m21+=1
    elif idade > 50:
        M50 +=1

print("Há %.2f pessoas menores de 21 anos" %m21)
print("Há %.2f pessoas maiores de 50 anos" %M50)
