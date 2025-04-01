#-*- coding: UTF-8 -*-

print ("Olá usuário. Me dê a distância que irá percorrer viajando e a velocidade média e te direi a duração do percurso")
distancia = float(input("Digite o valor em quilômetros da distância do percurso"))
velocidade = float(input("Digite a velocidade média em km/h do carro"))

percurso = distancia / velocidade

print("O tempo de viagem do carro será de: %2.f horas" %percurso)

                  
