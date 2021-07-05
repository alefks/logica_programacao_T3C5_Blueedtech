nome = str(input("Digite seu nome: "))
sexo = int(input("Escolha seu sexo:\n1 - Masculino\n2 - Feminino\nR: "))

while sexo != 1 and sexo != 2:
    print()
    sexo = int(input("Você digitou algo errado!\nEscolha seu sexo:\n1 - Masculino\n2 - Feminino\nR: "))
if sexo == 1:
    sexo = "Masculino"
if sexo == 2:
    sexo = "Feminino"

idade = int(input("Digite sua idade: "))

#TERMINAR!!!!