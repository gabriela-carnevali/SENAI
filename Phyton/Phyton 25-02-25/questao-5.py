# -*- coding: UTF-8 -*-

print("Digite o sexo de uma pessoa e eu direi quantas são do sexo masculino. Digite 0 para parar a contagem")

cont = 0
resposta = 0
M = 0 
F = 0
while True:
    resposta = input("Digite o sexo feminino (F) ou masculino (M): ")
    if resposta == "0":
        print(" Você escolheu sair, tchau!")
        break 
    elif resposta == "m" or resposta == "M":
        cont +=1
       

print("A resposta é: ", cont)
