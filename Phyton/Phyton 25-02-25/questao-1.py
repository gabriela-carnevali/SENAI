#-*- coding: UTF-8 -*-

inicio = 0
while True:
    num = int(input("""Coloque números e direi o triplo deles.
Para sair, digite -999: """))
    if num == -999:
        print("Você escolheu sair, tchau!")
        break
    inicio = num * 3
    print (inicio)
