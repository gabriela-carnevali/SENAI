#-*- coding: UTF-8 -*-

print("Olá usuário! Digite seu peso e sua altura e calcularei seu IMC")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * 2)

if imc < 20:
    print(" Você está abaixo do peso")
elif imc >=20 and imc >= 25:
    print(" Seu peso é normal")
elif imc >25 and imc <= 30:
    print(" Você está sobre peso")
elif imc >30 and imc <= 40:
    print("Você está obeso")
else:
    print("Você é obeso mórbido")
      
