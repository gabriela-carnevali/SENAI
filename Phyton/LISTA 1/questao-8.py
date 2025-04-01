# -*- coding: UTF-8 -*-

print("Olá usuário!  Diga o seu salário bruto e o valor da prestação e te direi se o empréstimo pode ou não ser concedido")

salario = float(input("Digite o valor de seu salário: "))
prestacao = float(input("Digite o valor da prestação: "))
salario_porcentagem = salario * 30 / 100

if prestacao > salario_porcentagem:
    print("O empréstimo não pode ser concedido")
else:
    print("O empréstimo pode ser concedido")
