# -*- coding: UTF-8 -*-

print ("Diga a velocidade do seu carro e te direi se foi multado e o valor de sua multa")
velocidade = float(input("Digite a velocidade de seu carro: "))
if velocidade > 80:
    print (" Você foi multado")
else:
    print ("Você respeitou o limte de velocidade")

ultrapassagem = velocidade - 80
multa = ultrapassagem * 5
float(input(" O valor multa é: R$%6.2f" % multa))


