# -*- coding: UTF-8 -*-

print ("Diga a quantidade de quilômetros percorridos por seu carro e quantidade de dias que o alugou e te direi o preço a pagar")
distancia = float(input("Digite o valor em quilômetros que o carro percorreu"))
dias_alugados = int(input("Diga a quantidade de dia que alugou o carro"))

valor_pagar = distancia * 0.15 + dias_alugados * 60

print (" O valor a ser pago é de R$", valor_pagar)
