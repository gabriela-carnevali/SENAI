# -*- coding: UTF-8 -*-

print("Digite números inteiros e te direi a soma dos números pares e ímpares. O programa para quando entrar um número maior que mil")

soma_par = 0
soma_impar = 0

while True:
    valor = int(input("Digite um valor: "))
    if valor > 1000:
        print("Você escolheu sair, tchau!")
        break
    elif valor %2 == 0:
        soma_par = soma_par + valor
    elif valor %2 != 0:
        soma_impar = soma_impar + valor
        
print("A soma dos números pares é: ", soma_par)
print("A soma dos números ímpares é: ", soma_impar)
