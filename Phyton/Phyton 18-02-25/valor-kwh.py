# -*- coding: UTF-8 -*-

print ("Diga a quantidade de KWh consumidas e o tipo de instalação e te direi o valor da sua conta")
consumo = float(input("Digite a quantidade de KWh consumida: "))
instalacao = input(""" Digite o tipo de instalação, sendo:
R para residências
I para indústrias
C para comércios: """)
if instalacao == "R":
    if consumo <= 500:
        pagamento = consumo * 0.40
    else:
        pagamento = consumo * 0.65
elif instalacao == "C":
    if consumo <= 2500:
        pagamento = consumo * 0.55
    else:
        pagamento = consumo * 0.60
elif instalacao == "I":
    if consumo <= 10000:
        pagamento = consumo * 0.55
    else:
        pagamento = consumo * 0.60

print ("O valor a ser pago será: R$%6.2f " % pagamento)
