# -*- coding: UTF-8 -*-

print("Digite um número e eu calcularei o fatorial dele")

num = int(input("Digite um valor: "))

fatorial = 1

for i in range (num,1,-1):
   fatorial = fatorial * i
   
print(fatorial)
    
