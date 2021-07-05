gols_separados = []
contador = 1
total_gols = 0

nome_jogador = input("Digite o nome do jogador: ").capitalize()

partidas_jogador = int(input("Digite a quantidade de partidas jogadas: "))
print()

for i in range(partidas_jogador):
    gols_partida = int(input(f"Quantidade de gols da partida {contador}: "))
    print()
    gols_separados.append(gols_partida)
    total_gols += gols_partida
    contador += 1

print(nome_jogador)
print(gols_separados)

dicionario_golseparado = {}

for index,i in enumerate(gols_separados):
    dicionario_golseparado[f"Partida {index + 1}"] = i

dicionario_golseparado["total"] = total_gols

print(dicionario_golseparado)