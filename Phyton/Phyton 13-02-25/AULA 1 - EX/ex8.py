#-*- coding: UTF-8 -*-

print("Vamos calcular o valor do carro alugado")

quant_km = float(input("Digite a quantidade de km percorridos: "))

quant_dias = int(input("Digite a quantidade de dias: "))

preco_a_pagar = quant_km * 0.15 + quant_dias * 60

print("O valor total a pagar é de: %.2f" %preco_a_pagar)
