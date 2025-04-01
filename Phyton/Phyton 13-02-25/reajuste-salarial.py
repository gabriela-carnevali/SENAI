#-*- coding: UTF-8 -*-

print (" Digite o valor do seu salário e a percentagem do aumento eu calcularei o aumento e o valor do novo salário")
salario = float(input("Digite o valor de seu salário: "))
percentagem = float(input("Digite a percentagem do reajuste: "))

salario_novo = salario + salario/100 * percentagem
aumento = salario_novo - salario

print("O seu salário, com o reajuste é: ", salario_novo)
print ("O valor do reajuste é: ", aumento)
