#-*- coding: UTF-8 -*-

print("Vamos calcular o tempo de vida perdido fumando cigarros!")

cigarros_dia = int(input("Digite a quantidade de cigarros consumidos por dia: "))

anos_fumados = float(input("Digite a quantiade de anos: "))

cigarros_anos = cigarros_dia * anos_fumados * 365

minutos_perdidos = cigarros_anos * 10

total_dias = minutos_perdidos // 1440

#print("A quantidade de dias perdidos foram de: ", total_dias)

print(f"O resultado é: {total_dias:.2f}")
