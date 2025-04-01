# -*- coding: UTF-8 -*-

print("Olá usuário! Me dê dois valores e te direi a soma de números ímpares entre eles")

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

def n_impares (a,b):
    soma = 0
    for i in range (a, b + 1):
        if i % 2 != 0:
            soma += i
    return (soma)

print (n_impares(a,b))
    
