aluno = {}

nome_aluno = str(input("Digite o nome do aluno: "))
nota_aluno = float(input("Digite a nota do aluno: "))
aluno["Nome"] = nome_aluno
aluno["Nota"] = nota_aluno

if nota_aluno >= 7:
    aluno["Situação"] = "Aprovado"
elif nota_aluno >=5 and nota_aluno <= 6.9:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

print(aluno)