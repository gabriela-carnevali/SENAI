# -*- coding: UTF-8 -*-

print("Olá usuário. Diga sua idade e eu classficarei sua faixa etária")

idade = int(input("Digite sua idade: "))

if idade < 2:
    print("A faixa etária é: Bebê")
elif idade >= 2 and idade <12:
    print("A faixa etária é: Criança")
elif idade >= 12 and idade < 23:
    print("A faixa etária é: Adolescente")
elif idade >= 23 and idade < 70:
    print("A faixa etária é: Adulto")
else:
    print("A faixa etária é: Idoso")
