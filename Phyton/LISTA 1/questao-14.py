# -*- coding: UTF-8 -*-

print("Olá usuário. Diga o valor de um produto e eu te darei o valor de venda com lucro")
produto = float(input("Digite o valor do produto: "))

if produto < 20:
    valor_final = produto + produto * 45 /100
    print("O valor será: ", valor_final)
else:
    valor_final = produto + produto * 30 / 100
    print("O valor será: ", valor_final)
