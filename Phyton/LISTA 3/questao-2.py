# -*- coding:UTF-8 -*-

print("Olá usuário! Diga um número e te direi o resultado da multiplicação de seus dígitos")

def produtofinal(x):
    calculo = 1
    while x >= 1:
        calculo *= x%10
        x = int(x/10)
    return calculo

num = int(input("Digite o número: "))
print (f"O resultado é {produtofinal(num)}")
