#-*- coding: UTF-8 -*-

#Exemplo 1
"""
num = 2

if num > 3:
    print ("Valor maior que 3")
"""

#Exemplo 2
"""
a = int(input("Digite o primeiro valor"))
b = int(input("Digite o segundo valor:"))

if a > b:
    print("O primeiro número é maior")

if b > a:
    print ("O segundo número é maior")
"""

#Exemplo 3
"""
idade = int(input("Digite a idade do seu carro"))
if idade <= 3:
    print ("Seu carro é novo")
else:
    print ("Seu carro é velho")
"""

#Exemplo 4
"""
minutos = int(input("Quantos minutos você utilizou esse mês: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
            preco = 0.15
print ("Você vai pagar esse mês: R$%6.2f" %(minutos * preco))
"""

#Exemplo 5
"""
categoria = int(input("Digite a categoria do produto"))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print ("Categora inválida, digite um valor entre 1 e 5!")
                    preco = 0
print ("O preço do produto é: R$%6.2f" % preco)
"""

#Exercício 6
"""
categoria = int(input("Digite a categoria do produto"))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preco = 0
print("O preço do produto é: R$%6.2f"  % preco)
"""
