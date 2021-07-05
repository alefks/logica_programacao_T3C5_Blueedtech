# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class modelarpessoa():
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self):
        
        total = self.idade * 0.5
        return f"Você cresceu {total}"
        # if self.idade < 21:
        #     total = self.anos_envelhecer * 0.5
        #     self.altura += total
        #     return f"Você cresceu {total} cm!\nAltura: {self.altura}"
        # else:
        #     return f"Você não pode mais crescer, pois a idade {self.anos_envelhecer} é igual ou maior que 21!"
    
    def envelhecer(self, anos_envelhecer):
        self.anos_envelhecer = anos_envelhecer
        self.idade += self.anos_envelhecer
        return f"Você envelheceu {self.anos_envelhecer} anos!\nIdade atual: {self.idade}"
    
    def engordar(self, qnt_engordar):
        self.qnt_engordar = qnt_engordar
        self.peso += self.qnt_engordar
        return f"Engordou {self.qnt_engordar} kg.\nPeso atual: {self.peso}"
    
    def emagrecer(self, qnt_emagrecer):
        self.qnt_emagrecer = qnt_emagrecer
        self.peso -= self.qnt_emagrecer
        return f"Emagreceu {self.qnt_emagrecer} kg.\nPeso atual: {self.peso}"

nome_pessoa = input("Digite seu nome: ")
print()
idade_pessoa = int(input("Digite sua idade: "))
print()
peso_pessoa = float(input("Digite seu peso: "))
print()
altura_pessoa = float(input("Digite sua altura: "))
print()
pessoa = modelarpessoa(nome_pessoa, idade_pessoa, peso_pessoa, altura_pessoa)

resp = "s"
while resp == "s":
    entrada = int(input("Digite uma opção:\n1 - Crescer\n2 - Envelhecer\n3 - Engordar\n4 - Emagrecer\nR: "))

    if entrada == 1:
        print(pessoa.crescer())
    elif entrada == 2:
        r2 = int(input("Digite quantos anos deseja envelhecer: "))
        pessoa.envelhecer(r2)
    elif entrada == 3:
        r3 = float(input("Digite o quanto deseja engordar: "))
        pessoa.engordar(r3)
    elif entrada == 4:
        r4 = float(input("Digite o quanto deseja emagrecer: "))
        pessoa.emagrecer(r4)
    else:
        print("Você digitou algo errado!")