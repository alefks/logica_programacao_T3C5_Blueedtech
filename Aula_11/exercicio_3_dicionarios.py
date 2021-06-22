### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos = {"batata":5, "leite":10, "Água": 7, "Maçã":0}

escolha = print("1 - Batata\n2 - Leite\n3 - Água\n4 - Maçã\nPesquise um item: ").lower()

produtos.get(escolha, f"O produto {escolha} não existe!")

quant_escolha = 0
if escolha in produtos:
    if 