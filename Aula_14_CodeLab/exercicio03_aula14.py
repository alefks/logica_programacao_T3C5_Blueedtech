# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
# sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir 
# o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    taxaImpostoConvertida = (custo * taxaImposto) / 100
    precoTotal = custo + taxaImpostoConvertida
    return f"Taxa de imposto: {taxaImpostoConvertida}\nValor total: {precoTotal}"

taxa = float(input("Digite a taxa de imposto em porcentagem: "))
custoProduto = float(input("Digite o custo do produto: "))
resultado = somaImposto(taxa,custoProduto)
print()
print(resultado)