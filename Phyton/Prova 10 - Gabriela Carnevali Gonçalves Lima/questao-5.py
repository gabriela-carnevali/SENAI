# coding: UTF-8 -*-

print("Olá usuário! Digite a quantidade de anos de serviço e o valor da compra na loja para funcionários da empresa de Zézinho Funilarias e te direi o valor do desconto de acordo com os anos de serviço")

anos = int(input("Digite o valor inteiro de anos trabalhados: "))
compra = int(input("Digite o valor inteiro da compra: "))
desconto = 0

if anos < 5:
    print ("Você digitou uma quantidade de anos que não pode receber desconto.")
elif anos >= 5 and anos <= 10:
    desconto = compra * 5 / 100
else:
    desconto = compra * 10 / 100

print ("O valor do desconto é: ", desconto)
print ("O valor total da compra é: ", compra - desconto)
