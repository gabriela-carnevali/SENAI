# -*- coding: UTF-8 -*-

print(" Olá usuário! Me forneça uma quantidade de dias, horas, minutos e segundos e converterei esse valor para segundos")
dias = int(input("Digite a quantidade de dias"))
horas = int(input("Digite o valor de horas"))
minutos = int(input("Digite o valor de minutos"))
segundos = int(input("Digite o valor de segundos"))

soma = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print ("O total de tempo, em segundos, é igual a: ", soma)
