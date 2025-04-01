# coding:UTF-8 -*-

print ("Olá usuário! Me dê 10 números e eu os mostrarei em ordem inversa")

vetor = []

for i in range(10):
    num = float(input("Digite um valor: "))
    vetor.append (num)

for v in range (1,11):
     print (vetor[-v])
