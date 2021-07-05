# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calculadoraSalario(horasTotais, salarioPorHora, horasExtras):
    
    horasTotais = horasTotais - horasExtras
    if horasTotais > 40:
        horasTotais = horasTotais + (horasExtras * 1.5)
    
    salarioTotal = horasTotais * salarioPorHora
    return salarioTotal

hrsTotais = float(input("Digite a quantidade total de horas trabalhadas: "))
salarioHora = float(input("Digite o salário por hora: "))
hrsExtras = float(input("Digite as horas extras: "))
result = calculadoraSalario(hrsTotais, salarioHora, hrsExtras)
print(result)