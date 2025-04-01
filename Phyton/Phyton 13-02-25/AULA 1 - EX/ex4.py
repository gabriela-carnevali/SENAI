#-*- coding: UTF-8 -*-

print("Farei o calcule de aumento de salário, com a porcentagem")

salario = float(input("Digite o salário: "))

porcentagem = float(input("Digite a porcentagem de aumento: "))

aumento = salario * porcentagem / 100

novo_salario = aumento + salario

#novo_salario = salario + salario * porcentagem /100

print("O aumento é de: ", aumento)

print("o novo salário é de: ", novo_salario)
