# coding:UTF-8 -*-

V = [9,8,7,12,0,13,21]
P = []
I = []

for i in range (len(V)):
    if V[i] % 2 == 0:
        P.append (V[i])

    else:
        I.append (V[i])

print (f" Os números pares são: {P} e os ímpares {I}")
    
