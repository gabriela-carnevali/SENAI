# -*- coding: UTF-8 -*-

print("Olá usuário! Me dê o preço de uma mercadoria e o percentual de desconto e te direi o valor do desconto e o preço que irá pagar")
mercadoria = float(input("Digite o valor da mercadoria"))
desconto = int(input("Digite a percentagem de desconto"))

preco_pagar = mercadoria - (mercadoria/100) * desconto
valor_desconto = preco_pagar - mercadoria

print (" O valor que será pago após o desconto será: ", preco_pagar)
print (" O valor do desconto é: ", valor_desconto)
