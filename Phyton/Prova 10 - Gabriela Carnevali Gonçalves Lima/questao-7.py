# coding:UTF-8 -*-

print("Olá usuário! Me diga o valor da área da base a da altura de uma pirâmide e eu te direi seu volume!")

area = float(input("Digite o valor da área da base da pirâmide: "))
altura = float(input("Digite o valor da altura da pirâmida: "))

def volume (area,altura):
    volume = (1 / 3) * area * altura
    return volume

print(" O valor do volume é: ", volume(area, altura))
