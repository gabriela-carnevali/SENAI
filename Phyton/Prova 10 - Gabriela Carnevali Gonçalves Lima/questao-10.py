# -*- coding: UTF-8 -*-

print ("Olá usuário! Me diga um valor de capital, a taxa de juros ao mês e o tempo em meses e eu calcularei o juros simples do seu empreendimento!")

capital = float(input("Digite o valor de seu capital: "))
juros = float(input("Digite o valor do juros ao mês em decimal (5% igual a 0.05, por exemplo): "))
tempo = float(input("Digite o tempo, em meses, da aplicação: "))

juros_simples = capital * juros * tempo
resultado = capital + juros_simples

print ("O valor do juros de seu empreendimento após o tempo de aplicação é: %.2f" % juros_simples)
print ("O capital final de seu empreendimento será de: %.2f" % resultado)
