lista = []
teste = 0

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)


    resposta = str(input("Você deseja adicionar outro número?\n(S/N): ").upper())

    if resposta != "S" and resposta != "N":
        print("Você digitou algo errado.")
        resposta = str(input("Você deseja adicionar outro número?\n(S/N): ").upper())
    
    if resposta == "S":
        while True:
            teste = int(input("Digite um valor: "))
            if teste in lista:
                print(f"O valor {teste} já existe na lista!")
            else:
                lista.append(teste)
                resposta = str(input("Deseja adicionar outro número?\n(S/N): ").upper())
                if resposta == "N":
                    break

    
    if resposta == "N":
        break

lista.sort()
print(lista)