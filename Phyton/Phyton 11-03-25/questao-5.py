# -*- coding: UTF-8 -*-

import math

print("Olá usuário! Digite o valor de um raio de círculo e lhe direi a área")

raio = float(input("Digite o valor do raio: "))

def area ():
    return (math.pi * raio ** 2)

print ("A área é igual a: %.2f " % area())
