# -*- coding: UTF-8 -*-

print("Olá usuário! Digite um número e eu te direi se ele é múltiplo de três ou não")

valor = float(input("Digite o valor: "))

if valor %3 == 0:
    print("O valor é divisível por 3")
else:
    print("O valor não é divisível por 3")
