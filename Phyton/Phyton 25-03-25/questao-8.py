# -*- coding:UTF-8 -*-

print("Olá usuário! Me diga a idade e altura de cinco pessoas e eu os mostrarei na ordem inversa que me foi dada")

Idade = []
Altura = []

for i in range (5):
    idade = int(input("Digite sua idade: "))
    altura = int(input("Digite sua altura: "))

    Idade.append (idade)
    Altura.append (altura)

for i in range(1,6):
    idade = Idade[-i]
    altura = Altura[-i]
    
print (f"A idade em ordem inversa é: {Idade[-i]}")
print (f"A altura em ordem inversa é: {Altura[-i]}")
