# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def verificaNumero(n1):
    if n1 > 0:
        resp = "P"
        return resp
    if n1 < 0:
        resp = "N"
        return resp
    if n1 == 0:
        resp = "0"
        return resp

numero = float(input("Digite um número: "))
resultado = verificaNumero(numero)
print(resultado)