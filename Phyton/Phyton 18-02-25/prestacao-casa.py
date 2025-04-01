# -*- coding: UTF-8 -*-

print("Envie informações e direi se o emprpestimo para sua casa será aceito")

valor_casa = float(input("Digite o valor da casa que quer comprar"))
salario = float(input("Digite o valor do seu salário"))
anos = float(input("Digite a quantidade de anos a pagar"))
prestacao = anos / salario
meses = anos / 12

if prestacao > salario * 30 / 100:
    print ("O valor da prestação não pode ser maior que 30% do seu salário, por favor, escolha outra quantidade de empréstimos para ser aprovado")
else:
    print ("Seu empréstimo foi aprovado!")
    
