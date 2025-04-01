# -*- coding:UTF-8 -*-

print("Olá usuário! Digite um número e te direi a quantidade de dígitos que ele tem.")

num = int(input("Digite um número: "))
contagem = 0

def cont (num):
    global contagem 
    while num >= 1:
        num = num / 10
        contagem +=1
       
cont(num)
print ("O número de dígitos é igual a: ", contagem)
