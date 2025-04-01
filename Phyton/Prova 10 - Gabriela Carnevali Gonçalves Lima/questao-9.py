# -*- coding: UTF-8 -*-

print("Informe três valores reais e informarei qual tipo de triângulo seria")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))


if valor1 == valor2 and valor2 != valor3 and valor1 != valor3:
    print ("O triângulo é isóceles (dois lados iguais)") 
elif valor1 == valor2 and valor1 == valor3 and valor2 == valor3:
    print("O triângulo é equilátero (todos os lados iguais)")
elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
    print (" O triângulo é escaleno (nenhum lado igual")
else:
    valor1 + valor2 > valor3 or valor2 + valor3 > valor1 or valor1 + valor3 > valor2
    print ("Os valores não podem formar um triângulo")
  
