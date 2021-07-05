# Simulador de Votação - Alessandro Kobashigawa (T3C5)

def autoriza_voto(ano_nascimento):
    idade = 2021 - ano_nascimento

    if idade < 16:
        autorizacao = f"--> {nome_pessoa}, seu voto foi NEGADO!"
        return autorizacao
    
    elif idade >= 18 and idade < 70:
        autorizacao = f"--> {nome_pessoa}, seu voto é OBRIGATÓRIO!"
        return autorizacao
    
    elif idade >= 16 and idade < 18:
        autorizacao = f"--> {nome_pessoa}, seu voto é OPCIONAL!"
        return autorizacao
    
    elif idade >= 70:
        autorizacao = f"--> {nome_pessoa}, seu voto é OPCIONAL!"
        return autorizacao

def votacao(autorizacao, voto):
    
    if "OBRIGATÓRIO" in autorizacao or "OPCIONAL" in autorizacao:
        
        for i in [1,2,3,4,5]:
            
            if voto == i:
                escolha_pessoa = numeros_urna.get(i)
                print()
                resp = str(input(f"Você confirma seu voto para: {escolha_pessoa}?\n(S/N): ").lower())
            
                while resp != "s" and resp != "n":
                    print()
                    resp = str(input(f"Você digitou algo errado!\nVocê confirma o voto para: {escolha_pessoa}?\n(S/N): ").lower())
            
                if resp == "s":
                    pontos_adicionar = pontos_urna.get(escolha_pessoa) + 1
                    print(pontos_adicionar)
                    pontos_urna[escolha_pessoa] = pontos_adicionar
                    print()
                    return f"{nome_pessoa}, seu voto foi computado com sucesso!\n--> Sessão encerrada."
            
                if resp == "n":
                    print()
                    return f"{nome_pessoa}, seu voto foi DESCONSIDERADO.\n--> Sessão encerrada."
                
    if "NEGADO" in autorizacao:
        return f"{nome_pessoa}, você ainda não pode votar.\n--> Sessão encerrada."

numeros_urna = {1:"João",2:"Pedro",3:"Carlos",4:"Voto nulo",5:"Voto em branco"}
pontos_urna = {"João":0,"Pedro":0,"Carlos":0,"Voto nulo":0,"Voto em branco":0}

continuar = "s"
while continuar == "s":
    print()
    print("--> Seja bem vindo(a) a Urna de Votação Python!")
    print()

    nome_pessoa = input("Digite seu nome: ").title()
    while nome_pessoa.isalpha() is False:
        print()
        nome_pessoa = input("--> Por favor, digite apenas letras e sem espaços!\nDigite seu nome: ").capitalize()
    
    verificar_nascimento = input("Digite seu ano de nascimento: ")
    while verificar_nascimento.isdigit() is False or len(verificar_nascimento) > 4 or len(verificar_nascimento) < 4:
        print()
        verificar_nascimento = input("--> Erro! Verifique se você digitou corretamente o ano.\nDigite seu ano de nascimento novamente: ")

    nascimento = int(verificar_nascimento)
    autorizacao_pessoa = autoriza_voto(nascimento)

    if "OBRIGATÓRIO" in autorizacao_pessoa:
        print()
        print(autoriza_voto(nascimento))
        print()
        voto_pessoa = int(input("Opções de Voto:\n1 - João\n2 - Pedro\n3 - Carlos\n4 - Voto Nulo\n5 - Voto em Branco\nDigite o número: "))
        
        while voto_pessoa not in numeros_urna.keys():
                print()
                voto_pessoa = int(input("Você digitou algo errado!\nDigite o número do seu candidato: "))
        print(votacao(autorizacao_pessoa,voto_pessoa))

    elif "OPCIONAL" in autorizacao_pessoa:
        print()
        print(autoriza_voto(nascimento))
        opcional_resp = str(input("Você deseja votar?\n(S/N): ").lower())
        
        while opcional_resp != "s" and opcional_resp != "n":
            print()

            opcional_resp = str(input("Você digitou algo errado!\nVocê deseja votar?\n(S/N): ").lower())
        
        if opcional_resp == "s":
            print()
            voto_pessoa = int(input("Opções de Voto:\n1 - João\n2 - Pedro\n3 - Carlos\n4 - Voto Nulo\n5 - Voto em Branco\nDigite o número: "))
            
            while voto_pessoa not in numeros_urna.keys():
                print()
                voto_pessoa = int(input("Você digitou algo errado!\nDigite o número do seu candidato: "))
            print(votacao(autorizacao_pessoa,voto_pessoa))

    elif "NEGADO" in autorizacao_pessoa:
        voto_pessoa = ""
        print()
        print(votacao(autorizacao_pessoa,voto_pessoa))

    print()
    continuar = input("Deseja iniciar uma nova votação?\n(S/N): ")
    if continuar != "s" and continuar != "n":
        print()
        continuar = input("--> Erro!\nDeseja iniciar uma nova votação?\n(S/N): ")

print()
print("--> Quantidade de votos finais:")
for key, value in pontos_urna.items():
    print(f"{key}: {value} voto(s)")
print()

dic_final = pontos_urna.copy()
dic_final.pop("Voto nulo")
dic_final.pop("Voto em branco")

vencedor_nome = max(dic_final,key=dic_final.get)
vencedor_valor = dic_final.get(vencedor_nome)

empates = [[k for k,v in dic_final.items() if v == vencedor_valor]]

if vencedor_valor == 0:
    print("--> NENHUM candidato venceu!")
    exit()

elif len(empates[0]) == 1:
    print(f"--> O candidato {empates[0][0]} VENCEU!")
elif len(empates[0]) == 2:
        print(f"--> Os candidatos {empates[0][0]} e {empates[0][1]} EMPATARAM!")  
elif len(empates[0]) == 3:
        print(f"--> Os candidatos {empates[0][0]}, {empates[0][1]} e {empates[0][2]} EMPATARAM!")