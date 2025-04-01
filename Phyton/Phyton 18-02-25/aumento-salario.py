# -*- coding: UTF-8 -*-

print ("Diga seu salário e eu calcularei o valor do aumento")
salario = float(input("Digite o valor de seu salário"))

if salario > 1250:
    aumento = salario * 10 / 100
else:
    salario <= 1250
    aumento = salario * 15 / 100
salario_novo = salario + aumento

print (" O aumento do seu salário é igual a: R$%6.2f" % aumento)
print ("Seu novo salário é igual a: ", salario_novo)
