'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

print("Para parar de digitar valores, digite 'sair'.")

valores_unicos = []

while True:
    entrada = input("Digite um valor numérico: ") 
    
    if entrada.lower() == "sair":
        break

    if not entrada.lstrip('-').isdigit():  
        print("Por favor, digite apenas números ou 'sair'.")
        continue

    numero = int(entrada)
    
    if numero not in valores_unicos:
        valores_unicos.append(numero)

valores_unicos.sort()

print(valores_unicos,",")