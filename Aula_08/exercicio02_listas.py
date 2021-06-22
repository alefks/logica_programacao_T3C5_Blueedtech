#2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
contagem = 0

for i in perguntas:
    print(i)
    resposta = str(input("Digite sua resposta: ").upper())

    while resposta != "S" and resposta != "N":
        print("")
        print("Você digitou algo errado!")
        print(i)
        resposta = str(input("Digite sua resposta: ").upper())
    
    if resposta == "S":
        contagem+=1
    
if contagem == 5:
  print(f"Você é o assassino! {contagem} pontos.")
  
if contagem == 3 or contagem == 4:
  print(f"Você é cúmplice! {contagem} pontos.")
    
if contagem == 2:
  print(f"Você é suspeito! {contagem} pontos.")

if contagem == 1 or contagem < 1:
  print(f"Você é inocente! {contagem} pontos.")