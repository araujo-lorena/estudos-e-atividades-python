""" Escreva um programa que peça dois números ao usuário e, se o segundo número for zero, 
capture a exceção ZeroDivisionError e imprima uma mensagem amigável."""

def divisao_de_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2

        print(f"O resultado da divisão é: {resultado}")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        
divisao_de_numeros()



#Outra forma de fazer:


def divisao_de_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")  
        return resultado

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        
divisao_de_numeros()



    