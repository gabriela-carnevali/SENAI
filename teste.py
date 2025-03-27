print ("Hello world!")

cont = 0
while True:
    num = int(input("Digite um valor: "))
    if num < 0:
        print("Só podem existir valores positivos")
        break 
    else: 
        cont += 1
    media = num + num / cont 

print ("A média é: %.2f" % media)
print ("Oi Celso")
