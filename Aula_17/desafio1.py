# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado. Não esqueça que os lançamentos são feitos de forma randômica.

import random

sorteio_moedas = ["Cara","Coroa"]

escolha_usuario = ["Dados","Moedas"]
sorteio = ""

class lançador:
    
    def __init__(self, escolha_objeto):
        None

    def sorteiomoedas(self):
            sorteio = random.choice(sorteio_moedas)
            return f"O programa sorteou: {sorteio}!"
    
    def sorteiodados(self):
            sorteio = random.randint(1,6)
            return f"O programa sorteou: {sorteio}"

a = input("Opções:\n- Dados\n- Moedas\nR: ").lower()
escolha = lançador(a)

r = "s"
while r == "s":
    if a == "moedas":
        print(escolha.sorteiomoedas())
        break
    elif a == "dados":
        print(escolha.sorteiodados())
        break
    else:
        print("Você digitou algo errado!")
        break