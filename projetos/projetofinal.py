# Projeto final - As aventuras de Gustavo na Europa

import time
import sys
import random

#Funçao responsavel por printar com flush e sleep as falas e narracao da história
def print_diferente(lista):
    if "Correio" and "Gustavo" in lista:
        for i in lista:
            print(f"{i}", end="", flush=True)
            time.sleep(0.1)
    else:
        for i in lista:
            print(f"{i}", end="", flush=True)
            time.sleep(0.3)

situacao1_cruzeiro = [""]
#Mensagens com o sleep 0.1
msgs_slow01 = ["--> Correio Eletrônico: 1 nova mensagem.\n", "\nGustavo: Que email é esse?","\nGustavo: Deixa eu dar uma olhada...\n","\n--> Correio Eletrônico:\nRemetente: Lisboa Tech\nAssunto: Resultado da entrevista de emprego para desenvolvedor sênior.\n\nMensagem: \nParabéns, Gustavo! Seu desempenho durante a entrevista foi excepcional e queremos você na nossa equipe. Iremos mandar sua passagem, e deixamos a seu critério escolher se irá de cruzeiro ou avião.\nEstaremos esperando sua resposta! \n\nGrato, \nCEO da Lisboa Tech.","\n\n\nGustavo: Preciso decidir logo!\n"]
#Mensagens com o sleep 0.3
msgs_slow03 = ["\nAbrindo email...\n","\n\nNo dia seguinte...\n"]

print_diferente(msgs_slow01[0])
print_diferente(msgs_slow01[1])
time.sleep(1)
print_diferente(msgs_slow01[2])
print_diferente(msgs_slow03[0])
time.sleep(3)
print_diferente(msgs_slow01[3])
time.sleep(3)
print_diferente(msgs_slow01[4])
time.sleep(3)
print_diferente(msgs_slow03[1])
time.sleep(3)

r = "s"
dia = 1
dias_remanescentes = 30 - dia
resp = ""

while r == "s":
    print()
    print(f"Dia {dia}. Você tem ainda tem {dias_remanescentes} dia(s)!")
    print()
    resp = input("Gustavo: Acho que vou escolher...\n\n1 - Cruzeiro\n2 - Avião\n\nResposta (digite 1 ou 2): ")