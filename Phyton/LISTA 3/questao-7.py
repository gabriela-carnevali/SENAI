# -*- coding:UTF-8 -*-

print("Olá usuário! Escolha dois números e a operação matemática desejada e farei a conta para você")


def soma (num1, num2):
    print ("A soma dos valores é: ", num1 + num2)

def subtracao (num1,num2):
    print ("A subtração dos valores é: ", num1 - num2)

def multiplicacao (num1,num2):
    print ("A multiplicação dos valores é: ", num1 * num2)

def divisao (num1,num2):
    print ("A divisão dos valores é: ", num1 / num2)


num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
operacao = str(input("""Escolha a operação matemática, sendo "+", "-", "*" e "/" os sinais de cada operação: """))

if operacao == "+":
    soma (num1,num2)
elif operacao == "-":
    subtracao (num1,num2)
elif operacao == "*":
    multiplicacao (num1,num2)
elif operacao == "/":
    divisao (num1,num2)
else:
    print("Você digitou um valor não correspondente, escolha outro valor.")
