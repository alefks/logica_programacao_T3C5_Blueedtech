### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos = {"Batata":5, "Leite":10, "Água": 7, "Maçã":0}

escolha = input("1 - Batata\n2 - Leite\n3 - Água\n4 - Maçã\nPesquise um item: ").lower()

produtos.get(escolha, f"O produto {escolha} é inválido!")

quant_escolha = int(input("Digite a quantidade desejada: "))

if escolha in produtos:
    if 

#TERMINAR!!!!!!!!