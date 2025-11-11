''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

opcao = 0  

while opcao != 5:
    print('''\nEscolha uma das opções abaixo:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print("A soma entre",x,"e",y,"é igual a",x + y)
    elif opcao == 2:
        print("A multiplicação entre",x,"e",y,"é igual a",x * y)
    elif opcao == 3:
        print("O maior valor entre",x,"e",y,"é",max(x, y))
    elif opcao == 4:
        print("Informe os números novamente:")
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print("Finalizando o programa... Até logo!")
    else:
        print("Opção inválida. Tente novamente.")
