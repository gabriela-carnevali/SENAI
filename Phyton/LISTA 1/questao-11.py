# -*- coding: UTF-8 -*-

print(" Digite suas duas notas e te direi se foi aprovado, reprovado ou está de recuperação")

valor1 = float(input("Digite a primeira nota: "))
valor2 = float(input("Digite a segunda nota: "))

media = valor1 + valor2 / 2

if media < 3:
    print ("Você foi reprovado")
elif media >3 and media <=7:
    print ("Você está de recuperação")
else:
    media > 7 and media <10
    print ("Você foi aprovado")
