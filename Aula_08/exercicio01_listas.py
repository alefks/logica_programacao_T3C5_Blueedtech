# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
L = [5, 7, 2, 9, 4, 1, 3]
print(L)
print("")

# a) tamanho da lista.
tamanho_lista = len(L)
print(f"O tamanho da lista é {tamanho_lista}.")

# b) maior valor da lista.
maior_valor = max(L)
print(f"O maior valor da lista é {maior_valor}.")

# c) menor valor da lista.
menor_valor = min(L)
print(f"O menor valor da lista é {menor_valor}.")

# d) soma de todos os elementos da lista
soma = sum(L)
print(f"A soma de todos os valores é {soma}.")

# e) lista em ordem crescente.
L.sort()
print(f"Em ordem crescente: {L}")

# f) lista em ordem decrescente.
L.sort(reverse=True)
print(f"Em ordem decrescente: {L}")