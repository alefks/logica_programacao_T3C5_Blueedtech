# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def calcularIMC(altura,peso):
    total = peso / altura**2
    return total

alt = float(input("Digite sua altura em metros: "))
kg = float(input("Digite seu peso em kg: "))
resultado = calcularIMC(alt,kg)
print(f'Seu IMC é: {resultado:.2f}')