#-*- coding: UTF-8 -*-

print("vou calcular o desconto da sua mercadoria")

preco = float(input("digite o valor do produto: "))

percentual = float(input("Digite o percentual para desconto: "))

desconto = preco * percentual / 100

novo_valor = preco - desconto

#novo_valor = preco - preco * percentual / 100

print("O valor de desconto é de: ", desconto)

print("O %.2f novo valor do produto é de:  " %novo_valor)
