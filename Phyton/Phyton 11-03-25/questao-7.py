# -*- coding: UTF-8 -*-

print ("Olá usuário! Me diga o custo de um produto e a taxa de imposto a ser aplicada e direi o valor final")

taxaImposto = float(input("Digite o valor da taxa a ser aplicada no produto: "))
custo = float(input("Digite o valor do produto antes da taxa: "))

def somaImposto ():
    return (custo + custo * taxaImposto / 100)

print ("O valor final do produto é: %.2f" % somaImposto())
