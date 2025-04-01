# -*- coding:UTF-8 -*-

print ("Olá usuário! Digite um número de 1 a 10 e direi a tabuada dele")

def tabuada (num):
    for i in range (0,11):
        print(f"{num} x {i} = {i*num}")

num = int(input("Digite um número inteiro de 1 a 10: "))
print ()
tabuada (num)
