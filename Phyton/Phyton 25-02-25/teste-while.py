# -*- coding: UTF-8 -*-

"""
cont = 1
while cont <= 3:
    print(cont)
    cont+=1
    #cont = cont + 1

----------------------------------------------------------------------------------

fim = int(input("Defina o valor final para a quantidade de repetições"))

cont = 1

while cont <= fim:
    print (cont)
    #cont+=1
    cont = cont + 1

-----------------------------------------------------------------------------------

fim = int(input("Digite o último número a imprimir"))

x = 0
while x <= fim:
    if x % 2 == 0:
        print (x)
    x += 1

-----------------------------------------------------------------------------------

x = 1
while x <= 50:
    if x % 3 == 0:
        print (x)
    x += 1
    
------------------------------------------------------------------------------------

n = int(input("Tabuada de: "))

x = 0

while x <= 10:
    print (f' {n} * {x} = {n*x}')
    #print (n, "*", x, "=", (n * x))Outra maneira de fazer
    x += 1

-----------------------------------------------------------------------------------

x = 1
soma = 0
while x <= 10:
    n = int(input(" Digite o %d número: " % x))
    soma += n
    x += 1
print ("Soma: %d" % soma)

----------------------------------------------------------------------------------


x = 1
soma = 0
while x <= 5:
    n = int(input(" Digite o %i número: " % x))
    soma += n
    x += 1
print("Média: %5.2f" % (soma/5))

OU

----------------------------------------------------------------------------------

fim = int(input("Defina quantas vezes vai repetir: "))

x = 1
soma = 0
while x <= fim:
    n = int(input(" Digite o %i número: " % x))
    soma += n
    x += 1
print("Média: %5(casas antes da vírgula).2f" % (soma/fim))
#OU
print (f"Média: {soma/ fim:.2f}")

--------------------------------------------------------------------------------

s = 0
#while True: OU
while 1:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    if v == 0:
        break
    s += v
print (f"A soma é: %i " % s)

-------------------------------------------------------------------------------

cont = 0
acum = 0

while True:
    valor = float(input("Digite valores e no final lhe darei a média. Digite um valor negativo para sair"))
    if valor < 0:
        print ("Você escolheu sair, tchau!")
        break
    acum = acum + valor
    cont = cont + 1
  

print ("Média é igual a: ", acum/cont)
    
---------------------------------------------------------------------------------------------

"""

tabuada = 1
while tabuada <= 10:
    n = 0
    print ("Tabuada %i " % tabuada)
    while n <= 10:
        print ("%i * %i = %i "(tabuada, n, tabuada * n))
    tabuada = tabuada + 1
