#Projeto 02 - Jokenpo

from random import randint

resposta = "s"

while resposta == "s":
    print("Bem vindo ao Python Jokenpo!")
    rodadas = int(input("Quantas partidas iremos jogar? "))
    print(f"Ok, jogaremos {rodadas} rodadas!")
    print("")

    pontos_cpu = 0
    meus_pontos = 0

    for i in range(rodadas):
        sua_escolha = str(input("Escolha (Pedra/Papel/Tesoura): ").upper())
        
        sorteio = randint(1,3)
        if sorteio == 1:
            escolha_cpu = "PEDRA"
            escolha_cpu1 = ["TESOURA"]
        if sorteio == 2:
            escolha_cpu = "PAPEL"
            escolha_cpu1 = ["PEDRA"]
        if sorteio == 3:
            escolha_cpu = "TESOURA"
            escolha_cpu1 = ["PAPEL"]

        while sua_escolha != "PEDRA" and sua_escolha != "PAPEL" and sua_escolha != "TESOURA":
            print("Você digitou algo errado!")
            sua_escolha = str(input("Digite usa escolha novamente:\n(Pedra/Papel/Tesoura): ").upper())
        
        if sua_escolha == escolha_cpu:
            print("")
            print(f"EMPATE! Eu também escolhi {escolha_cpu}!")
            print("")
        if sua_escolha != escolha_cpu and sua_escolha in escolha_cpu1:
            print("")
            print(f"Você PERDEU! Eu escolhi {escolha_cpu}!")
            print("")
            pontos_cpu+=1

        if sua_escolha != escolha_cpu and sua_escolha not in escolha_cpu1:
            print("")
            print(f"Você VENCEU! Eu escolhi {escolha_cpu}!")
            print("")
            meus_pontos+=1

    if meus_pontos > pontos_cpu:
        print("")
        print(f"----> Você VENCEU!\nSeus pontos: {meus_pontos}\nPontos do computador: {pontos_cpu}")
        print("")
    if meus_pontos == pontos_cpu:
        print(f"----> EMPATE!\nSeus pontos: {meus_pontos}\nPontos do computador: {pontos_cpu}")
        print("")
    if pontos_cpu > meus_pontos:
        print(f"----> Você PERDEU!\nSeus pontos: {meus_pontos}\nPonto do computador: {pontos_cpu}")
        print("")

    resposta = str(input("Você deseja jogar novamente?\n(S/N): ").lower())
    while resposta != "s" and resposta != "n":
        resposta = str(input("Você escreveu algo errado! Deseja jogar novamente?\n(S/N): ").lower())