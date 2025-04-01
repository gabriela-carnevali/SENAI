#-*- coding: UTF-8 -*-

print("Vamos converter todos os valores de entrada em segundos")

dias = int(input("Digite a qtd de dias: "))
horas = int(input("Digite a qtd de horas: "))
minutos = int(input("Digite a qtd de minutos: "))
segundos = int(input("Digite a qtd de segundos: "))

cdias = dias * 24 * 60 * 60
#cdias = dias * 86400

choras = horas * 60 * 60
#choras = horas * 3600

cminutos = minutos * 60

total_seg = cdias + choras + cminutos + segundos
#total_seg = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print("O total em segundos é de: ", total_seg)
