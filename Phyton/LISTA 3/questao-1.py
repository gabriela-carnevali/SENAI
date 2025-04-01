# -*- coding: UTF-8 -*-

import math
print ("Olá usuário! Me dê a altura e o raio de um cilindro e eu te direi o volume")

raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))

def volume ():
    return (math.pi * raio ** 2 * altura)

print (" O volume é: %.2f" % volume())
