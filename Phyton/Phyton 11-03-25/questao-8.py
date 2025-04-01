# -*- coding: UTF-8 -*-

print ("Olá usuário! Digite sua idade e eu trarei sua classe eleitoral")

idade = int(input("Digite sua idade"))

def eleitoral ():
    if idade < 16:
        return "Não eleitor"
    elif idade > 15 and idade < 18:
        return "Eleitor facultativo"
    elif idade > 65:
        return "Eleitor facultativo"
    elif idade > 18 and idade < 65:
        return "Eleitor obrigatório"

print ("Sua classe eleitoral é: ", eleitoral())
