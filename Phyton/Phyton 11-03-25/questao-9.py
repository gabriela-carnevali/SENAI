# -*- coding: UTF-8 -*-

print ("Olá usuário! Digite o valor inteiro de sua nota, e te direi em qual conceito você se encontra")

nota = int(input("Digite o valor de sua nota: "))

def media ():
    if nota < 3:
        return "Conceito E"
    elif nota >= 3 and nota <= 5:
        return "Conceito D"
    elif nota >= 6 and nota <= 7:
        return "Conceito C"
    elif nota >= 8 and nota <= 9:
        return "Conceito B"
    elif nota == 10:
        return "Conceito A"

print ("Seu conceito é: ", media())
