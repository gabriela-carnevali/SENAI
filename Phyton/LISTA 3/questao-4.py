# -*- coding: UTF-8 -*-

print("Olá usuário! Digite um número inicial e eu farei uma contagem regressiva.")

num = int(input("Digite um número: "))

def regressiva (num):
    for i in range (num, 0, -1):
        print (i)

regressiva (num)

print ("Feliz Ano Novo!")
