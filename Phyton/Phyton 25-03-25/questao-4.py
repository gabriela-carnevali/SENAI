# coding:UTF-8 -*-

print("Olá usuário! Digite 10 caractéres minúsculos e lhe direi quantas consoantes existem")

vetor = []
consoantes = 0

for i in range (10):
    letra = input("digite caracteres: ")
    vetor.append(letra)

for letra in vetor:
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        consoantes += 1

print(consoantes)
