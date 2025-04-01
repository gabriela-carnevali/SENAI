# coding:UTF-8 -*-

T = [-10,-8,0,1,2,5,-2,-4]

menor_temperatura = T[0]
maior_temperatura = T[0]

for i in T:
    if i < menor_temperatura:
        menor_temperatura = i
    elif i > maior_temperatura:
        maior_temperatura = i

soma = 0

for i in T:
    soma += i
media = soma / len(T)

print(f" A maior temperatura é: {maior_temperatura}°C, e a menor temperatura é: {menor_temperatura}°C")
print(f" A média é igual a: {media}")








































































































