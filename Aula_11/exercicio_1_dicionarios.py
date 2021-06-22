#Exercício 1 - Criar dicionário a partir de uma lista, e cada valor correspondente é N ao quadrado.

numeros = [1, 4, 5, 6, 7, 9]
dicnumeros1 = {}

for i in numeros:
    dicnumeros1[i] = i**2

print(dicnumeros1)