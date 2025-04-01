# -*- coding: UTF-8 -*-

print("Olá usuário! Digite um número e lhe direi se ele é primo ou não")

num = int(input("Digite um número: "))

def primo (num):
    cont = 0
    for i in range (1, num):
        if num % i == 0:
            cont += 1
    if cont == 1:
        print (" O número é primo")
    else:
        print ("O número não é primo")

primo(num)
