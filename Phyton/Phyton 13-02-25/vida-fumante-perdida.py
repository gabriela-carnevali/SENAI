# -*- coding: UTF-8 -*-

print("Olá usuário, digite a quantidade de cigarros que fu,a por dia e por quantos anos você fumou e te direi quantos dias de vida perdeu")
cigarros_dia = int(input("Digite a quantidade de cigarros que fuma por dia"))
anos_fumando = int(input("Digite a quantos anos você fuma"))

reducao_vida = 365 * cigarros_dia * anos_fumando * 10
mudanca_dias = reducao_vida / 1440

print (" A quantidade de dias perdidos é de: %.2f " %mudanca_dias)
