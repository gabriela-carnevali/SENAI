# -*- coding: UTF-8 -*-

print("Me dê três notas e o número de faltas e lhe direi se foi aprovado, reprovado por falta ou reprovado por média")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
n_falta = int(input("Digite a quantidade de faltas: "))

media = nota1 + nota2 + nota3 / 3
falta = 80 * 25/100

if media < 7:
    print ("Você foi aprovado")
elif n_falta > falta:
    print ("Você foi reprovado por falta")
else:
    print ("Você foi reprovado por média")
