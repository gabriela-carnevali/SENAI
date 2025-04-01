# -*- coding:UTF-8 -*-

#variável criada fora do def
resultado = 0

# função criada para fazer um soma
def soma ():
    #chamando a variável RESULTADO como GLOBAL
    global resultado
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    resultado = num1 + num2

#chamando a função SOMA
soma ()

#printando a variável RESULTADO que é GLOBAL (após executar a função)
print("O resultado é: ", resultado)

#criei uma variável com o mesmo nome da função (NÃO TEM PROBLEMA)
soma = 3
print(soma)
