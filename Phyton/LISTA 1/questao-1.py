# -*- coding: UTF-8 -*-

print("Olá usuário! Escolha dois números e eu farei a adição. Caso o valor seja superior a vinte, somarei oito unidades. Caso seja menor, subtrairei cinco unidades")


valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))

soma = valor1 + valor2

if soma > 20:
    total = soma + 8
else:
    if soma <= 20:
        total = soma - 5

print ("O resultado é: ", total)
