"""Faça um programa que solicite ao usuário um número inteiro. Use um bloco try...except para 
capturar um ValueError caso o usuário digite algo que não possa ser convertido em inteiro e,
 em seguida, imprima uma mensagem de erro."""

def solicitar_numero_inteiro():
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número: {numero}")
        
    except ValueError:
        print("Erro: Você não digitou um número inteiro válido.")

solicitar_numero_inteiro()