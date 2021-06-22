# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

n = int(input("Digite um número: "))
conta = 0

for i in range(1, n+1):
    if (n % i) == 0:
        conta+= 1

print(conta)