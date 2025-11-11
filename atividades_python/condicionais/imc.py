""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMCe mostre seu status, e 
acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida"""

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Desnutrição (Abaixo do peso)"
elif imc < 25:
    status = "Peso ideal"
elif imc < 30:
    status = "Sobrepeso"
elif imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

print("Seu IMC é:", imc,"e seu status é:", status)
