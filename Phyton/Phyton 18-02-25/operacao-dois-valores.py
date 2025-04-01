# -*- coding: UTF-8 -*-

print("Digite dois número e escolha a operação que deseja realizar e te direi o resultado da operação solicitada")
valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
operacao = input("Escolha a operação: ")

if operacao == "+":
    resultado = valor_1 + valor_2
elif operacao == "-":
    resultado = valor_1 - valor_2
elif operacao == "*":
    resultado: valor_1 * valor_2
elif operacao == "/":
    resultado = valor_1 / valor_2

print("O valor final será: ", resultado)
