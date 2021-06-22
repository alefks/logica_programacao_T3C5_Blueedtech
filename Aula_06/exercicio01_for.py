#01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u

palavra = str(input("Digite algo: ")).upper()
contagem = 0

for x in palavra:
    if x == "A":
        contagem+= 1

print(f"Quantidade de a(s): {contagem}")