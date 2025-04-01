# coding:UTF-8 -*-

print("Olá usuário! Me dê quatro notas e te darei a média delas")

L = []
cont = 0

for i in range (1,5):
    nota = float(input("Digite sua nota: "))
    cont += nota
    L.append(nota)

media = cont / 4
print (media)
