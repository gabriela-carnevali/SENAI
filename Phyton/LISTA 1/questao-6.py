# -*- coding: UTF-8 -*-

print("Digite dois números inteiros (sem vírgula) e te direi se o primeiro número é divisível pelo segundo")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 %valor2 == 0:
    print("O segundo valor é divisível pelo primeiro")
else:
    print("O segundo valor não é divisível pelo primeiro valor")
