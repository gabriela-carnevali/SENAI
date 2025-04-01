# -*- coding: UTF-8 -*-

print(" Me dê valores e direi qual é o maior e qual é o menor. O programa termina quando um número negativo for digitado")

valor = float(input("Digite o valor: ")

maior = valor
menor = valor

while True:
    valor = float(input("Digite o valor: "))
    if valor < 0:
        print("Você escolheu sair, tchau!")
        break
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    

print("O maior valor é: ", maior)
print("O menor valor é: ", menor)
