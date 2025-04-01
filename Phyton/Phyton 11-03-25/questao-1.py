# -*- coding: UTF-8 -*-

print ("Olá usuário! Digite dois valores e eu direi o maior entre eles")

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))

def maior ():
    if num1 > num2:
        return num1
    else:
        return num2

print ("O maior valor é: ", maior())
