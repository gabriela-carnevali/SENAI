# -*- coding: UTF-8 -*-

print("Olá usuário! Digite um número positivo ou negativo. Caso ele seja positivo ou igual a zero, te direi a raiz. Caso seja negativo, te direi o quadrado")
valor = float(input("Digite o valor desejado: "))

import math
if valor >= 0:
    resultado = math.sqrt(valor)
else:
    resultado = valor ** 2

print("O resultado é igual a: %.2f" %resultado)
