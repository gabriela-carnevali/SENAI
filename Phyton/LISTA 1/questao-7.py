# -*- coding: UTF-8 -*-

print("Olá usuário! Digite o número de horas trabalhadas e direi seu salário líquido")

horas = int(input("Digite o número de horas trabalhadas"))
salario = horas * 19.50

if salario > 1500:
    resultado = salario - salario * 10/100     
else:
    resultado = salario

print("O resultado é igual a: ", resultado)
