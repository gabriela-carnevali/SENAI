# -*- coding: UTF-8 -*-

a = 5 # variável global

def muda_e_imprime():
 global a # variável global
 a = 7
 print("a dentro da função: %d" % a)

print("a antes de mudar: %d" % a)

muda_e_imprime()
print("a depois de mudar: %d" % a)
