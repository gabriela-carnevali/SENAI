# -*- coding:UTF-8 -*-

#Criando a lista (definndo valores com 0 apenas para ter a quantidade de itens
numeros = [0, 0, 0, 0, 0]
#Navegar pelo WHILE
x = 0

while x < 5:
    #Essa linha está pegando o valor para inserir na LISTA
 numeros[x] = int(input("Número %d: " % (x + 1)))
 x += 1
while True:
    #Essa lnha está pegando o valor do ÍNDICE para mostrar o valor inserido
 escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
 #Verificando saída do WHILE TRUE
 if escolhido == 0:
     break
    # Mostrando o valor de acordo com o índice, tirando 1 para agradar o usuário
 print ("Você escolheu o número: %d" % (numeros[escolhido - 1]))
