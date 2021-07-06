class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self,valor):
        valor_total = valor / self.valorLitro
        
        self.quantidadeCombustivel -= valor_total
        return f"Você pagou {valor:.2f} e abasteceu {valor_total:.1f} litros"
    
    def abastecerPorLitro(self, litro):
        valor_total_litros = litro * self.valorLitro

        self.quantidadeCombustivel -= litro
        return f"Você pagou {valor_total_litros:.2f} e abasteceu {litro:.2f}"
    
    def alterarValor(self,novoValor_litro):
        self.valorLitro = novoValor_litro
    
    def alterarCombustivel(self,novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade_combustivel):
        self.quantidadeCombustivel = novaQuantidade_combustivel

posto1 = bombaCombustivel("Gasolina", 4.10, 1000)

print(posto1.quantidadeCombustivel)

print(posto1.abastecerPorLitro(20))
print(posto1.quantidadeCombustivel)
print()
print(posto1.abastecerPorValor(82))
print(posto1.quantidadeCombustivel)