# -*- coding:UTF-8 -*-

print ("Olá usuário! Digite quatro valores em cada lista e farei uma lista final com todos os valores")

L1 = []
L2 = []
L3 = []

for i in range (4):
    valor = input("Digite valores: ")
    L1.append(valor)

for j in range (4):
    valor = input("Digite valores: ")
    L2.append(valor)

L3.extend(L1)
L3.extend(L2)

print(L3)
