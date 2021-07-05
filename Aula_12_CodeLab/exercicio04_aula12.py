perguntas = ["Digite seu nome: ", "Ano de nascimento: ", "Número Carteira de Trabalho (digite 0 caso não tenha): "]
trabalhador = {}

for x in perguntas:
    print(x)
    
    if "nome" in x:
        nome = str(input().capitalize())
        trabalhador["Nome"] = nome
    if "nascimento" in x:
        ano_nascimento = int(input())
        
        trabalhador["Ano de Nascimento"] = ano_nascimento
    if "Carteira" in x:
        numero_carteira = int(input())
        if numero_carteira != 0:
            ano_contratacao = int(input("Digite o ano de contratação: "))
            trabalhador["Ano de Contratação"] = ano_contratacao
            salario = float(input("Digite o seu salário: "))
            trabalhador["Salário"] = salario
        
        trabalhador["Número da Carteira de Trabalho"] = numero_carteira

idade = 2021 - ano_nascimento
idade_aposentadoria = (ano_contratacao + 35) - ano_nascimento

trabalhador["Idade"] = idade
trabalhador["Idade de Aposentadoria"] = idade_aposentadoria

print(trabalhador)