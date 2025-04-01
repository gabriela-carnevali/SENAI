# -*- coding:UTF-8 -*-

print("Olá usuário! Digite números positivos e negativos e eu lhe direi quantos de cada tipo você digitou. Se quiser sair do programa, digite 0!")


positivo = 0
negativo = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        print ("Você escolheu sair, tchau!")
        break
    elif num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        print("Você digitou um caractere inváido.")

print ("O quantidade de números positivos é: ", positivo)
print ("A quantidade de números negativos é: ", negativo)
