lista = []
pares = []
impares = []

valor = int(input("Digite um número: "))
lista.append(valor)

while True:
    resposta = input("Deseja adicionar outro número? (S/N): ").lower()
    while resposta != "s" and resposta != "n":
        resposta = input("Erro! Deseja adicionar outro número? (S/N): ").lower()
    
    if resposta == "s":
        valor = int(input("Digite outro número: "))
        lista.append(valor)
    if resposta == "n":
        break

for x in lista:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print(f"Lista completa: {lista}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")