# Projeto final - As aventuras de Gustavo na Europa

import time
import sys
import random

def print_diferente(lista):
    if "Correio" and "Gustavo" in lista:
        for i in lista:
            print(f"{i}", end="", flush=True)
            time.sleep(0.1)
    elif "Não acredito! Parabéns!" in lista[0]:
        for i in lista:
            print(f"{i}", end="", flush=True)
            time.sleep(0.1)
    else:
        for i in lista:
            print(f"{i}", end="", flush=True)
            time.sleep(0.3)

class Personagem:
    def __init__(self):
        self.malas_arrumadas = False
        self.ligacao_namorada = False
        self.github_atualizar = False
    
    def arrumarMalas(self):
        self.malas_arrumadas = True
        return self.malas_arrumadas

    def ligarNamorada(self):
        self.ligacao_namorada = True
        return self.ligacao_namorada

    def githubAtualizar(self):
        self.github_atualizar = True
        return self.github_atualizar

class Transporte:
    def printarTransporte(self):
        print("Estou em tal meio de transporte")

class Aviao(Transporte):
    def printarTransporte(self):
        print("Você está viajando na companhia aérea Fly Emirates. A vista aérea é incrível!")
        
class Cruzeiro(Transporte):
    def printarTransporte(self):
        print("Você está viajando no MSC Cruzeiros Portugal, com uma vista linda do mar!")

class Tempo:
    def __init__(self):
        self.__dia = 1
        self.__dias_remanescentes = 10
    
    def proximoDia(self):
        if self.__dia < 10:
            self.__dia +=1
        
        elif self.__dia == 10:
            print("Gustavo, você está no último dia!")
        else:
            pass
    
    def printarDia(self):
        print(f"Você está no dia {self.__dia} e restam {self.__dias_remanescentes - self.__dia} dia(s)!")
    
    @property
    def dia(self): 
        return self.__dia
    
    @dia.setter
    def dia(self, alterar_dia): 
        raise ValueError("Impossivel alterar o dia diretamente. O usuário deve, necessariamente, iniciar do 1° dia.")

situacao1_cruzeiro = [""]
#Mensagens com o sleep 0.1
msgs_slow01 = ["--> Correio Eletrônico: 1 nova mensagem.\n", "\nGustavo: Que email é esse?","\nGustavo: Deixa eu dar uma olhada...\n","\n--> Correio Eletrônico:\nRemetente: Lisboa Tech\nAssunto: Resultado da entrevista de emprego para desenvolvedor sênior.\n\nMensagem: \nParabéns, Gustavo! Seu desempenho durante a entrevista foi excepcional e queremos você na nossa equipe. Iremos mandar sua passagem, e deixamos a seu critério escolher se irá de cruzeiro ou avião.\nEstaremos aguardando sua resposta! \n\nGrato, \nCEO da Lisboa Tech.","\n\n\nGustavo: Preciso decidir logo!\n"]
#Mensagens com o sleep 0.3
msgs_slow03 = ["\nAbrindo email...\n","\n\nNo dia seguinte...\n"]

print_diferente(msgs_slow01[0])
print_diferente(msgs_slow01[1])
# time.sleep(1)
print_diferente(msgs_slow01[2])
print_diferente(msgs_slow03[0])
# time.sleep(3)
print_diferente(msgs_slow01[3])
# time.sleep(3)
print_diferente(msgs_slow01[4])
# time.sleep(3)
print_diferente(msgs_slow03[1])
# time.sleep(3)
 
r = "s"
x = 0
tempo = Tempo()
gustavo = Personagem()
contar_acoes = 0
acoes_dia = ["\n\nArrumando as malas...\n\n","\n\nLigando para a Nebulosa...\n\n","\n\nAtualizando o GitHub...\n\n"]
ligacao_nebulosa = ["A Nebulosa atendeu!","A Nebulosa não atendeu!"]
respostas_nebulosa = [["Não acredito! Parabéns!","Fico muito feliz por você, mas tenho que desligar agora.","Amanhã nos vemos!"], ['VAI VENDER CURSO!!','TA BÊBADO CARA!!']]

print()
tempo.printarDia()
resp = input("\n\nGustavo: Acho que vou escolher...\n\n1 - Cruzeiro\n2 - Avião\n\nResposta (digite 1 ou 2): ")

while resp != "1" and resp != "2":
        resp = input("\n\n- Você digitou algo errado!\n\nGustavo: Acho que vou escolher...\n\n1 - Cruzeiro\n2 - Avião\n\nResposta (1/2): ")

if resp == "1":
    print("\n\nCerto, então você irá de cruzeiro para Portugal!")
    situacao_escolhida = "cruzeiro"

if resp == "2":
    print("\n\nCerto, então você irá de avião para Portugal!")
    situacao_escolhida = "aviao"

while r == "s":
    print()
    resp_opcoesdia = input("\nOpções para fazer hoje:\n1 - Arrumar as malas\n2 - Ligar para a Nebulosa (apelido da parceira conjugal do herói)\n3 - Atualizar o GitHub\n\nResposta (1/2/3): ")

    while resp_opcoesdia != "1" and resp_opcoesdia != "2" and resp_opcoesdia != "3":
        resp_opcoesdia = input("\n\n- Você digitou algo errado!\n\nOpções para fazer hoje:\n1 - Arrumar malas\n2 - Ligar para a Nebulosa (apelido da parceira conjugal do herói)\n3 - Atualizar o GitHub\n\nResposta (1/2/3): ")

    if contar_acoes < 3:
        if resp_opcoesdia == "1":
            
            if gustavo.malas_arrumadas == True:
                print("\n\nSuas malas já estão arrumadas!\n\n")
                pass
            else:
                print_diferente(acoes_dia[0])
                gustavo.arrumarMalas()
                contar_acoes+=1
                print("Pronto, malas arrumadas!\n\n")
        
        if resp_opcoesdia == "2":
            print_diferente(acoes_dia[1])
            confirma_nebulosa = random.choice(ligacao_nebulosa)

            if "não atendeu!" in confirma_nebulosa:
                print(confirma_nebulosa)
                print()
            else:
                print(confirma_nebulosa)
                print()
                gustavo.ligarNamorada()
                contar_acoes+=1
                
                resp_nebulosa = input("1 - Contar que passou na entrevista e irá para Portugal\n2 - Falar que desistiu da carreira de Desenvolvedor Sênior e agora vai virar influencer e gravar dancinha para o TikTok\n\nResposta (1/2): ")
                
                while resp_nebulosa != "1" and resp_nebulosa != "2":
                    resp_nebulosa = input("- Você digitou algo errado!\n\n1 - Contar que passou na entrevista e irá para Portugal\n2 - Falar que desistiu da carreira de Desenvolvedor Sênior e agora vai virar influencer e gravar dancinha para o TikTok\n\nResposta (1/2): ")
                
                if resp_nebulosa == "1":
                    for i in range(3):
                        print_diferente(f"\nNebulosa: {respostas_nebulosa[0][i]}")
                
                if resp_nebulosa == "2":
                    for i in range(2):
                        print_diferente(f'\nNebulosa: {respostas_nebulosa[1][i]}')
                
        if resp_opcoesdia == "3":
            if gustavo.github_atualizar == True:
                print("\n\nSeu GitHub já está atualizado!\n\n")
            else:
                print_diferente(acoes_dia[2])
                gustavo.githubAtualizar()
                print("\n\nGitHub atualizado com sucesso!\n\n")
                contar_acoes+=1
    
        elif contar_acoes == 3:
            r = "a"